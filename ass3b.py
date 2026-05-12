import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]
    total_cost = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if node not in visited:
            visited.add(node)
            total_cost += weight
            print("Visited:", node, "Weight:", weight)

            for neighbor, w in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, neighbor))

    print("Total Cost of MST:", total_cost)


def main():
    graph = {}

    n = int(input("Enter number of nodes: "))

    for i in range(n):
        node = input(f"Enter node {i+1}: ")
        edges = int(input(f"Enter number of neighbors for {node}: "))
        graph[node] = []

        for j in range(edges):
            neighbor = input(f"Enter neighbor {j+1} of {node}: ")
            weight = int(input(f"Enter weight for edge {node} - {neighbor}: "))
            graph[node].append((neighbor, weight))

    start = input("Enter starting node: ")

    prim(graph, start)


if __name__ == "__main__":
    main()

# Enter number of nodes: 3

# Enter node 1: A
# Enter number of neighbors for A: 2
# Enter neighbor 1 of A: B
# Enter weight for edge A - B: 1
# Enter neighbor 2 of A: C
# Enter weight for edge A - C: 3

# Enter node 2: B
# Enter number of neighbors for B: 2
# Enter neighbor 1 of B: A
# Enter weight for edge B - A: 1
# Enter neighbor 2 of B: C
# Enter weight for edge B - C: 2

# Enter node 3: C
# Enter number of neighbors for C: 2
# Enter neighbor 1 of C: A
# Enter weight for edge C - A: 3
# Enter neighbor 2 of C: B
# Enter weight for edge C - B: 2

# Enter starting node: A