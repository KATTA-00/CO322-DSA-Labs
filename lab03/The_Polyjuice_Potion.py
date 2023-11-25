# CO322 Lab 03 E19
# Group Members - E/19/006 and E/19/129

# Input the value to search
value = int(input())

# Input the number of elements in the array
num = int(input())

# Input the array elements
arr = list(map(int, input().strip().split(" ")))

# bubble sort on a list
def bubble_sort(data):
    flag = True

    while flag:
        flag = False

        for j in range(len(data) - 1):
            # Swap adjacent elements if they are in the wrong order
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag = True

# Function to binary search on a sorted array
def binary_search(arr, value):
    l = 0
    r = len(arr)
    mid = (l+r)//2
    
    while (l < r):
        # Check if the middle element is the target value
        if arr[mid] == value:
            return mid
    
        # If the middle element is less than or equal to the target value, search the right half
        if arr[mid] <= value:
            l = mid + 1
        else:
            # If the middle element is greater than the target value, search the left half
            r = mid - 1
            
        mid = (l+r)//2
        
    # Check if the left pointer is within bounds and if the element at the left pointer is the target value
    if l < len(arr) and arr[l] == value:
        return l

    # If the target value is not found, return -1
    return -1
    
# Sort the array using bubble sort
bubble_sort(arr)

# Search for the index of the value using binary search
index = binary_search(arr, value)

# Check if the value is found and print the result
if index != -1:
    print("Bicorn Horn is present at index " + str(index))
else:
    print("Bicorn Horn is not found!")
