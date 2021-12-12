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

def solve(graph, lower, start, end, flag):
    def recursion(graph, head, lower, end, visited, flag, twice):
        if head == end:
            return 1
        if head in lower:
            if visited[head]:
                if flag:
                    if twice:
                        return 0
                    twice = True
                else:
                    return 0
            visited[head] = True
        return sum(recursion(graph, x, lower, end, deepcopy(visited), flag, twice) for x in graph[head])
    return recursion(graph, start, lower, end, {key: False for key in lower}, flag, False)


def main():
    f = open("input.txt", "r")
    start, end = "start", "end"
    graph, lower = create_graph(f.readlines(), start, end)
    print(solve(graph, lower, start, end, False)) #Part 1: 5576
    print(solve(graph, lower, start, end, True)) #Part 2: 152837
    f.close()

if __name__ == "__main__":
    main()