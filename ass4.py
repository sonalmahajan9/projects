#4th assignment-csp-queens
N = int(input("Enter number of Queens: "))
board = [[0 for i in range(N)] for j in range(N)]
left_row = [False] * N
upper_diagonal = [False] * (2 * N - 1)
lower_diagonal = [False] * (2 * N - 1)
def print_board():
    for row in board:
        for cell in row:
            if cell == 1:
                print("Q",end = " ")
            else:
                print(".",end = " ")
        print()
def solve(col):
    if col == N:
        return True
    for row in range(N):
        if(left_row[row] == False and lower_diagonal[row + col] == False and upper_diagonal[N - 1 + col - row] == False):
            board[row][col] = 1
            left_row[row] = True
            lower_diagonal[row + col] = True
            upper_diagonal[N - 1 + col - row] = True
            if solve(col + 1):
                return True
            board[row][col]=0
            lower_diagonal[row + col]=False
            left_row[row] = False
            upper_diagonal[N - 1 + col - row]=False
    return False

if solve(0):
    print("\nSolution Found")
    print_board()
else:
    print("No solution found")