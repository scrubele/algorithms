vertexes = set()


def read_from_file():
    with open('graph.txt') as f:
        data = f.readlines()
    graph = {}

    n = data.__len__()
    for i in range(1, n):
        nums = [int(n) for n in data[i].split()]
        graph = add_value(graph, nums[0], nums[1])
        graph = add_value(graph, nums[1], nums[0])
        vertexes.add(nums[0])
        vertexes.add(nums[1])

    return graph, n


def add_value(graph, x, y):
    try:
        z = graph[x]
    except KeyError:
        graph[x] = set()

    graph[x].add(y)
    return graph


def odd(st, parity):
    if st % 2 == 1:
        parity[0] += 1
    else:
        parity[1] += 1
    return parity


def dfs(graph, st, parity):
    print(st, end=" ")
    parity = odd(st, parity)

    try:
        vertexes.remove(st)
    except:
        pass

    for vertex in graph[st]:
        if vertex in vertexes:
            dfs(graph, vertex, parity)


def dfs_main(graph, n):
    tribes = []
    # print(graph)
    while vertexes:
        parity = [0, 0]
        # print(vertexes)
        dfs(graph, int(vertexes.pop()), parity)
        # print(parity)
        tribes.append(parity)
        print()
    print(tribes)
    return tribes


def count_pairs(tribes):
    count = 0
    n = tribes.__len__()
    for i in range(0, n):
        for j in range(i, n):
            if i != j:
                x = tribes[i][0] * tribes[j][1] + tribes[i][1] * tribes[j][0]
                count += x
    return count


if __name__ == '__main__':
    graph, n = read_from_file()
    tribes = dfs_main(graph, n)
    count = count_pairs(tribes)
    print(count)
