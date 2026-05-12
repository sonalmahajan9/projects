#4th assignment - csp- graph colourinh
graph = [[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]
m = 3
colors = [0] * len(graph)
def solve(node):
    if node == len(graph):
        return True
    for color in range(1,m + 1):
        safe = True
        for neighbour in range(len(graph)):
            if graph[node][neighbour] == 1 and colors[neighbour] == color:
                safe = False
                break
        if safe:
            colors[node] = color
            if solve(node +  1):
                return True
            colors[node] = 0
    return False
if solve(0):
    print("\nSolution Found:\n")
    for i in range(len(colors)):Bu
        print("Vertex",i,"->",colors[i])
else:
    print("\nNo solution exists")