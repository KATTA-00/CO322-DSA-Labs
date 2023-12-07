t = int(input())

def mergerSort(arr, start, end):

    mid = (start + end)//2
    print(arr[start:end], start, end, mid)

    if start < end and end-mid >= 2:
        mergerSort(arr, mid+1, end)

    if start < end and mid-start >= 2:
        mergerSort(arr, start, mid)

    

for _ in range(t):
    arr = list(map(int, input().strip().split()))

    mergerSort(arr, 0, len(arr)-1)
    print()


    # print(" ".join([str(i) for i in arr]))



