# Constant for maximum limit
MAX_LIMIT = 99999

# Read input for height and width of the grid
h = int(input())
w = int(input())

# Read input for start and end points
start = list(map(int, input().strip().split(" ")))
end = list(map(int, input().strip().split(" ")))

# Read the grid input
grid = [list(map(int, input().strip("[").strip("]").split(", "))) for i in range(h)]

# Initialize a 2D list to store the minimum distance to each cell
count = [[MAX_LIMIT] * w for i in range(h)]

# Define movement directions (up, down, right, left)
x_values = [1, -1, 0, 0]
y_values = [0, 0, 1, -1]

# Function to check if a given cell is valid and not blocked
def checkValid(x, y):
    if x < 0 or y < 0 or x >= h or y >= w or grid[x][y] == 0:
        return False
    
    return True

# Depth-first search
def dfs(x, y, c):
    # If the current count is already less than or equal to the stored count, return 1
    if count[x][y] <= c:
        return 1
    
    # Update the count for the current cell
    count[x][y] = c
    
    # If the current cell is the destination, return 0
    if x == end[0] and y == end[1]:
        return 0
    
    # Explore neighbors in all four directions
    for i in range(4):
        x_val = x + x_values[i]
        y_val = y + y_values[i]
        
        # Recursive call to DFS for valid neighbors
        if checkValid(x_val, y_val):
            dfs(x_val, y_val, c + 1)

# Start DFS from the given start point
dfs(start[0], start[1], 0)

# Print the minimum distance or a message if no path is found
if count[end[0]][end[1]] != MAX_LIMIT:
    print("The minimum distance is " + str(count[end[0]][end[1]]))
else:
    print("There is no possible path")
