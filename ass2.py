import heapq

# Goal State
goal_state = [[1,2,3],
              [4,5,6],
              [7,8,-1]]

# Heuristic: Misplaced Tiles
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != -1 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

# Find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == -1:
                return i, j

# Generate neighbors
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    moves = [(0,1), (0,-1), (1,0), (-1,0)]  # right, left, down, up

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

# Convert state to tuple (for hashing)
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# A* Algorithm
def astar(start):
    open_list = []
    heapq.heappush(open_list, (heuristic(start), 0, start, []))  
    # (f, g, state, path)

    closed_set = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal_state:
            print("\nSolution Found!\n")
            for step in path + [current]:
                for row in step:
                    print(row)
                print()
            return

        closed_set.add(to_tuple(current))

        for neighbor in get_neighbors(current):
            if to_tuple(neighbor) in closed_set:
                continue

            new_g = g + 1
            new_f = new_g + heuristic(neighbor)

            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [current]))

    print("No Solution Found")

# Input
start_state = []
print("Enter Start State (use -1 for blank):")
for i in range(3):
    row = list(map(int, input().split()))
    start_state.append(row)

# Run
astar(start_state)


# Test Cases
# 
# 1
# 2
# 3
# -1
# 4 
# 6
# 7 
# 5 
# 8 

# 1 
# 2 
# 3 
# 4 
# 5 
# 6 
# 7 
# 8
# -1