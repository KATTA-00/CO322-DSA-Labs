def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1
    j = end

    while True:
        while i <= j and arr[i] > pivot:
            i += 1

        while i <= j and arr[j] <= pivot:
            j -= 1

        if i <= j:
            swap(arr, i, j)
        else:
            break

    swap(arr, start, j)
    return j

def quick_sort_algo(arr, start, end):
    if (start < end):

        pivot_index = partition(arr, start, end)
        quick_sort_algo(arr, start, pivot_index-1)
        quick_sort_algo(arr, pivot_index+1, end)
    

def quick_sort(arr):
    quick_sort_algo(arr, 0, len(arr)-1)

num = int(input())

names = input().strip().split(" ")
bravery_scores = list(map(int, input().strip().split(" ")))

arr_dic = {}
arr_set = set(bravery_scores)

for i in arr_set:
    temp = []
    arr_dic[i] = temp
    
for i in range(num):
    arr_dic[bravery_scores[i]].append(names[i])

arr_sorted = list(arr_dic)

quick_sort(arr_sorted)
quick_sort(bravery_scores)
    
for i in arr_sorted:
    quick_sort(arr_dic[i])
 
names_sort = [j for i in [arr_dic[i] for i in arr_sorted] for j in i]
bravery_scores_sort = [i for i in bravery_scores]

print(names_sort)
print(bravery_scores_sort)

count = 0
for i in range(num):
    if count == 5:
        break
    if bravery_scores_sort[i] > 500:
        print(names_sort[i])
        count +=1