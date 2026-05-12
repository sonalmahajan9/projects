import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist


def main():
    graph = {}

    n = int(input("Enter number of nodes: "))

    # Input nodes
    for i in range(n):
        node = input(f"Enter node {i+1}: ")
        edges = int(input(f"Enter number of neighbors for {node}: "))
        graph[node] = []

        for j in range(edges):
            neighbor = input(f"Enter neighbor {j+1} of {node}: ")
            weight = int(input(f"Enter weight for edge {node} -> {neighbor}: "))
            graph[node].append((neighbor, weight))

    start = input("Enter starting node: ")

    result = dijkstra(graph, start)

    print("\nShortest distances from", start)
    for node in result:
        print(node, ":", result[node])


if __name__ == "__main__":
    main()


# Enter number of nodes: 3

# Enter node 1: A
# Enter number of neighbors for A: 2
# Enter neighbor 1 of A: B
# Enter weight for edge A -> B: 2
# Enter neighbor 2 of A: C
# Enter weight for edge A -> C: 1

# Enter node 2: B
# Enter number of neighbors for B: 1
# Enter neighbor 1 of B: C
# Enter weight for edge B -> C: 3

# Enter node 3: C
# Enter number of neighbors for C: 0

# Enter starting node: A