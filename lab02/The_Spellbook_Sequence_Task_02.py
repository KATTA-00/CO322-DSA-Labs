n, m = map(int , input().strip().split(" "))

arr1 = list(map(int , input().strip().split(" ")))

arr2 = list(map(int , input().strip().split(" ")))

arr1_tuples = []

for i in range(n-1):
    for j in range(i+1, n):
        arr1_tuples.append((arr1[i], arr1[j]))

arr2_tuples = []

for i in range(m-1):
    for j in range(i+1, m):
        arr2_tuples.append((arr2[i], arr2[j]))


edges = []

if n < m:
    arr = arr1
    n = len(arr)

    for i in arr1_tuples:
        if i in arr2_tuples:
            edges.append(i)
            arr2_tuples.remove(i)
    
else:
    arr = arr2

n = len(arr)

nodes = []
for i in range(n):
    temp = []
    nodes.append(temp)

for i in range(n-1):
    for j in range(i+1, n):
        if (arr[i], arr[j]) in edges:
            edges.remove((arr[i], arr[j]))
            nodes[i].append(j)

max_len = 0
max_arr = []

print(nodes)

def dfs(n, count, a):
    global max_len, max_arr
    print(n)
    print(count, a)

    if count > max_len:
        max_len = count
        max_arr = a

    for i in nodes[n]:
        temp = a.copy()
        temp.append(arr[i])

        dfs(i, count + 1, temp)

for i in range(n):
    print(i)
    dfs(i, 1, [arr[i]])

print(max_len)
print(max_arr)