from copy import deepcopy

def create_graph(lines, start, end):
    def add_edge(adj, x1, x2, start, end):
        try:
            if x1 != end and x2 != start:
                adj[x1].append(x2)
        except KeyError:
            adj[x1] = [x2]
    adj = {}
    for line in lines:
        x1, x2 = line.strip().split("-")
        add_edge(adj, x1, x2, start, end)
        add_edge(adj, x2, x1, start, end)
    return adj, [key for key in adj if key not in [start, end] and key != key.upper()]

def part1(graph, lower, start, end):
    def recursion(graph, head, lower, end, visited):
        if head == end:
            return 1
        if head in lower:
            if visited[head]:
                return 0
            visited[head] = True
        return sum(recursion(graph, x, lower, end, deepcopy(visited)) for x in graph[head])
    visited = {key: False for key in lower}
    return recursion(graph, start, lower, end, deepcopy(visited))

def part2(graph, lower, start, end):
    def recursion(graph, head, lower, end, visited, twice):
        if head == end:
            return 1
        if head in lower:
            if visited[head]:
                if twice:
                    return 0
                twice = True
            visited[head] = True
        return sum(recursion(graph, x, lower, end, deepcopy(visited), twice) for x in graph[head])
    visited = {key: False for key in lower}
    return recursion(graph, start, lower, end, deepcopy(visited), False)

def main():
    f = open("input.txt", "r")
    start, end = "start", "end"
    graph, lower = create_graph(f.readlines(), start, end)
    print(part1(graph, lower, start, end)) #Part 1: 5576
    print(part2(graph, lower, start, end)) #Part 2: 152837
    f.close()

if __name__ == "__main__":
    main()