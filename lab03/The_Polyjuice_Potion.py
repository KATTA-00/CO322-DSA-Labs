# Enter your code here. Read input from STDIN. Print output to STDOUT
# Group Members - E/19/006 E/19/129
value = int(input())

num = int(input())

arr = list(map(int, input().strip().split(" ")))

def bubble_sort(data):
    flag = True

    while flag:
        flag = False

        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag = True

dic = {}
for i in range(num):
    dic[arr[i]] = i
    
def binary_search(arr, value):
    l = 0
    r = len(arr)
    mid = (l+r)//2
    
    while (l<r):
        if arr[mid] == value:
            return mid
    
        if arr[mid] <= value:
            l = mid + 1
        else:
            r = mid - 1
            
        mid = (l+r)//2
        
        
    if l < len(arr) and arr[l] == value:
            return mid
            
    return -1
    
bubble_sort(arr)
index = binary_search(arr, value)

if index != -1:
    print("Bicorn Horn is present at index " + str(index))
else:
    print("Bicorn Horn is not found!")
