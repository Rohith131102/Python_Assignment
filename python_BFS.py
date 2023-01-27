from collections import deque
def solve( board):
  
  m, n = len(board), len(board[0]) # Dimensions for the board
  q = deque() # Loading a queue
  dx = (1,0,-1,0) #to move in x direction
  dy = (0,1,0,-1) #to move in y direction
# Traversing the borders and storing the cells with entry 'O' in queue
  for i in range(m):
    if board[i][0] == 'O':
      q.append((i, 0))         # Traversing [0][0] to [m-1][0] and [0][n-1] to [m-1][n-1]
    if board[i][n-1] == 'O':
      q.append((i, n-1))
  for j in range(n):
    if board[0][j] == 'O':
      q.append((0, j))         # Traversing [m-1][0] to [m-1][n-1] and [0][0] #to [0][n-1]
    if board[m-1][j] == 'O':
      q.append((m-1, j))
#BFS implementation
  while q:
  # Poping the vertices from front and changing every 'O' connecting to it
    row, col = q.popleft()
    board[row][col] = '$' #changing 'O' to '$'
    for i in range(len(dx)):
      new_row,new_col = row+dx[i],col+dy[i]
      if (0 <= new_row < m and 0 <= new_col < n and board[new_row][new_col] == 'O'):
        q.append((new_row,new_col))
# Traversing every element in board and If we come across Y we make it 'O' else we make it. X.
  for i in range(m):
    for j in range(n):
      if board[i][j] == '$':
        board[i][j] = 'O'                                                               #time complexity - O(m*n)
      else:                                                                             #space complexity - O(m*n)
        board[i][j] = 'X'

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print("Board before - ")
for i in board:
  for j in i:
    print(j,end = " ")
  print()
solve(board)
print("Board after changes - ")
for i in board:
  for j in i:
    print(j,end = " ")
  print()

