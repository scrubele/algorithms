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



if __name__ == '__main__':
    graph, n = read_from_file()
    print(graph)
    max = dfs_main(graph, n)
    print(max-1)
