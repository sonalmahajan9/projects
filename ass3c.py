def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    mst = []
    total_cost = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, w))
            total_cost += w

    print("\nEdges in MST:")
    for edge in mst:
        print(edge)

    print("Total Cost:", total_cost)


def main():
    vertices = []
    edges = []

    n = int(input("Enter number of vertices: "))

    for i in range(n):
        v = input(f"Enter vertex {i+1}: ")
        vertices.append(v)

    e = int(input("Enter number of edges: "))

    for i in range(e):
        u = input(f"Enter starting vertex of edge {i+1}: ")
        v = input(f"Enter ending vertex of edge {i+1}: ")
        w = int(input(f"Enter weight of edge {u}-{v}: "))
        edges.append((u, v, w))

    kruskal(vertices, edges)


if __name__ == "__main__":
    main()

# Enter number of vertices: 4
# Enter vertex 1: A
# Enter vertex 2: B
# Enter vertex 3: C
# Enter vertex 4: D

# Enter number of edges: 5

# Enter starting vertex of edge 1: A
# Enter ending vertex of edge 1: B
# Enter weight of edge A-B: 1

# Enter starting vertex of edge 2: A
# Enter ending vertex of edge 2: C
# Enter weight of edge A-C: 3

# Enter starting vertex of edge 3: B
# Enter ending vertex of edge 3: C
# Enter weight of edge B-C: 2

# Enter starting vertex of edge 4: B
# Enter ending vertex of edge 4: D
# Enter weight of edge B-D: 4

# Enter starting vertex of edge 5: C
# Enter ending vertex of edge 5: D
# Enter weight of edge C-D: 5