def solve(risks, source, target):
    import heapq
    def get_neighbours(graph, i, j):
        neighbours = []
        for x in (i-1, i+1):
            if 0 <= x < len(graph):
                neighbours.append((x,j))
        for y in (j-1, j+1):
            if 0 <= y < len(graph[i]):
                neighbours.append((i,y))
        return neighbours
    dist, queue = [], []
    for x in range(len(risks)):
        dist.append([float("inf") for _ in range(len(risks[x]))])
    dist[source[0]][source[1]] = 0
    queue.append((0, (source[0], source[1])))
    while queue != []:
        u = heapq.heappop(queue)
        if u[1] == target:
            return u[0]
        for v in get_neighbours(risks, u[1][0], u[1][1]):
            alt = u[0] + risks[v[0]][v[1]]
            if alt < dist[v[0]][v[1]]:
                dist[v[0]][v[1]] = alt
                heapq.heappush(queue, (alt, (v[0], v[1])))

def expand_graph(graph, factor):
    from copy import deepcopy
    def increment_line(line):
        line = deepcopy(line)
        for i in range(len(line)):
            line[i] = 1 if line[i] == 9 else line[i] + 1
        return line
    def increment_graph(graph):
        graph = deepcopy(graph)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                graph[i][j] = 1 if graph[i][j] == 9 else graph[i][j] + 1
        return graph
    new_graph, new_segment = deepcopy(graph), deepcopy(graph)
    for _ in range(factor - 1):
        new_segment = increment_graph(new_segment)
        new_graph += new_segment
    for i in range(len(new_graph)):
        new_line = deepcopy(new_graph[i])
        for _ in range(factor - 1):
            new_line = increment_line(new_line)
            new_graph[i] += new_line
    return new_graph

def main():
    f = open("input.txt", "r")
    graph = [[int(x) for x in line.strip()] for line in f.readlines()]
    print(solve(graph, (0,0), (len(graph[0]) - 1, len(graph) - 1))) #Part 1: 595
    new_graph = expand_graph(graph, 5)
    print(solve(new_graph, (0,0), (len(new_graph[0]) - 1, len(new_graph) - 1))) #Part 2: 2914
    f.close()

if __name__ == "__main__":
    main()