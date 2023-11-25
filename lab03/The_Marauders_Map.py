# Enter your code here. Read input from STDIN. Print output to STDOUT

h = int(input())
w = int(input())

start = list(map(int, input().strip().split(" ")))
end = list(map(int, input().strip().split(" ")))

grid = [list(map(int, input().strip("[").strip("]").split(", "))) for i in range(h)]

visited = [ [False] * w  for i in range(h) ]

x_values = [1, -1, 0, 0]
y_values = [0, 0, 1, -1]

def checkValid(x, y):
    if x < 0 or y < 0 or x >= h or y >= w or grid[x][y] == 0:
        return False
    
    return True

count = 0

def dfs(x, y):
    global count
    
    if visited[x][y]:
        return 1
        
    visited[x][y] = True
    
    if x == end[0] and y == end[1]:
        return 0
        
    count +=1 
    
    for i in range(4):
        x_val = x + x_values[i]
        y_val = y + y_values[i]
        
        if checkValid(x_val, y_val):
            if dfs(x_val, y_val) == 0:
                return 0
                

dfs(start[0], start[1])

if (visited[end[0]][end[1]]):
    print("The minimum distance is " + str(count))
else:
    print("There is no possible path")