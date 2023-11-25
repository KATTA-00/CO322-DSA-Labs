# Enter your code here. Read input from STDIN. Print output to STDOUT

h = int(input())
w = int(input())

start = list(map(int, input().strip().split(" ")))
end = list(map(int, input().strip().split(" ")))

grid = [list(map(int, input().strip("[").strip("]").split(", "))) for i in range(h)]

count = [ [-1] * w  for i in range(h) ]

x_values = [1, -1, 0, 0]
y_values = [0, 0, 1, -1]

def checkValid(x, y):
    if x < 0 or y < 0 or x >= h or y >= w or grid[x][y] == 0:
        return False
    return True


que = [start]

def bfs():
    if que == []:
        return 0

    x, y = que.pop(0)

    for i in range(4):
        x_val = x + x_values[i]
        y_val = y + y_values[i]
        
        if checkValid(x_val, y_val) and count[x_val][y_val] == -1:
            que.append((x_val, y_val))
            count[x_val][y_val] = count[x][y] + 1

            if x_val == end[0] and y_val == end[1]:
                return 0

    if bfs() == 0:
        return 0


count[start[0]][start[1]] = 0
bfs()
        
if (count[end[0]][end[1]] != -1):
    print("The minimum distance is " + str(count[end[0]][end[1]]))
else:
    print("There is no possible path")