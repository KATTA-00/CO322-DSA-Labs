# Enter your code here. Read input from STDIN. Print output to STDOUT

h = int(input())
w = int(input())

MAX_LIMIT = 99999

start = list(map(int, input().strip().split(" ")))
end = list(map(int, input().strip().split(" ")))

grid = [list(map(int, input().strip("[").strip("]").split(", "))) for i in range(h)]
count = [ [MAX_LIMIT] * w  for i in range(h) ]

x_values = [1, -1, 0, 0]
y_values = [0, 0, 1, -1]

def checkValid(x, y):
    if x < 0 or y < 0 or x >= h or y >= w or grid[x][y] == 0:
        return False
    
    return True

def dfs(x, y, c):
    if count[x][y] <= c:
        return 1
    
    count[x][y] = c
    
    if x == end[0] and y == end[1]:
        return 0
    
    for i in range(4):
        x_val = x + x_values[i]
        y_val = y + y_values[i]
        
        if checkValid(x_val, y_val):
            dfs(x_val, y_val, c+1)
                

dfs(start[0], start[1], 0)

if (count[end[0]][end[1]] != MAX_LIMIT):
    print("The minimum distance is " + str(count[end[0]][end[1]]))
else:
    print("There is no possible path")