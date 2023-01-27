def solve(board): 
    m=len(board) #dimensions
    n=len(board[0])
    # DFS
    def dfs(row,col):
        if row>=m or row<0 or col>=n or col<0 or board[row][col] != 'O':
            return
        board[row][col]='$'
        dfs(row+1,col) # Moving Down
        dfs(row,col+1) # Moving Right
        dfs(row-1,col) # Moving Up
        dfs(row,col-1) # Moving Left
# Traversing every element in board and If we come across 'O' we move it to dfs and change the connected 'O'
    for i in range(m):
        if board[i][0] == 'O':
            dfs(i,0)    # Traversing [0][0] to [m-1][0] and [0][n-1] to [m-1][n-1]
        if board[i][n-1] == 'O':
            dfs(i, n-1)
    for j in range(n):
        if board[0][j] == 'O':
          dfs(0, j)         # Traversing [m-1][0] to [m-1][n-1] and [0][0] #to [0][n-1]
        if board[m-1][j] == 'O':
          dfs(m-1, j)
    # Traversing every element in board and If we come across $ we make it 'O' else we make it X.
    for i in range(m):
        for j in range(n):
            if board[i][j]=='O':
                board[i][j]='X'
            if board[i][j]=='$':
                board[i][j]='O'  
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print("Board before captures - ")
for i in board:
   for j in i:
      print(j,end = " ")
   print()
solve(board)
print("Board after captures - ")
for i in board:
    for j in i:
        print(j,end=" ")
    print()

