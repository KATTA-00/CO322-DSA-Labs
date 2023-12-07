t = int(input())

def swap(arr):
    if arr[0] > arr[1]:
        temp = arr[0]
        arr[0] = arr[1]
        arr[1] = temp

def combine(arr, start, mid, end):
    arr_left = arr[start:mid]
    arr_right = arr[mid:end+1]

    if len(arr_left) == 2:
        swap(arr_left)
    if len(arr_right) == 2:
        swap(arr_right)

    arr_new = []
    i = 0
    j = 0

    while i < len(arr_left) and j < len(arr_right):
        if arr_left[i] < arr_right[j]:
            arr_new.append(arr_left[i])
            i += 1
        else:
            arr_new.append(arr_right[j])
            j += 1

    arr_new.extend(arr_left[i:])
    arr_new.extend(arr_right[j:])

    for i in range(len(arr_new)):
        arr[start + i] = arr_new[i]


def merge_sort(arr, start, end):

    if start < end:
        mid = (start + end) // 2

        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        combine(arr, start, mid+1, end)

for _ in range(t):
    arr = list(map(int, input().strip().split()))

    merge_sort(arr, 0, len(arr))
    
    print(" ".join(map(str, arr)))
