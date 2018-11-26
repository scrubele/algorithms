vertexes = set()


def read_from_file():
    with open('graph.txt') as f:
        data = f.readline()
    graph = {}

    input = data.split()
    n = input.__len__()
    for i in range(0, n):
        for j in range(0, n):
            if input[i][j] == 'Y':
                element = 1
                graph = add_value(graph, i, j)
                vertexes.add(i)
                vertexes.add(j)
    return graph, n


def add_value(graph, x, y):
    try:
        z = graph[x]
    except KeyError:
        graph[x] = set()

    graph[x].add(y)
    return graph


def dfs_local(graph, start_vertex, local_vertexes):
    print(start_vertex, end=" ")

    try:
        local_vertexes.remove(start_vertex)
    except:
        pass

    for vertex in graph[start_vertex]:
        if vertex in local_vertexes:
            print("l", end=" ")
            print(vertex, end=" ")

    return local_vertexes


def dfs(graph, start_vertex, total):
    try:
        vertexes.remove(start_vertex)
    except:
        pass

    # print("vertex" + str(start_vertex))

    for vertex in graph[start_vertex]:
        # print("vertexes", end=" ")
        # print(graph[start_vertex])
        try:
            total.add(vertex)
            # print(graph[vertex])
            total = total.union(graph[vertex])
            # print(str(vertex) + "total", end=" ")
            # print(total)

        except RuntimeError:
            print()

    return total, start_vertex


def dfs_main(graph, n):
    # print
    max = 0
    while vertexes:
        # print(vertexes)
        total = set()

        total, v = dfs(graph, int(vertexes.pop()), total)
        if total.__len__() > max:
            max = total.__len__()
        # print(v, end=" ")
        # print(total)

    return max


if __name__ == '__main__':
    graph, n = read_from_file()
    print(graph)
    max = dfs_main(graph, n)
    print(max-1)
