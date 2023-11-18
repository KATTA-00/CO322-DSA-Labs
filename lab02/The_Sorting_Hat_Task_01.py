# def swap(arr, i, j):
#     temp = arr[i]
#     arr[i] = arr[j]
#     arr[j] = temp

# def partition(arr, start, end):

#     pivot = arr[start][0]
#     i = start
#     j = end
#     print(pivot)

#     while i<j:

#         while arr[i][0] >= pivot and i < end:
#             i += 1


#         while arr[j][0] < pivot and j > start+1:
#             j -= 1

#         if i>=j:
#             break

#         swap(arr, i, j)

#     swap(arr, start, j)

#     print(arr)

#     return j



# def quick_sort_algo(arr, start, end):
#     print(start, end)
#     print(arr)
    
#     if (start < end):

#         pivot_index = partition(arr, start, end)
#         print(">> ")
#         print(arr)
        
#         print(">>>>>>")
#         quick_sort_algo(arr, start, pivot_index-1)
#         print(">>>>>>>>>>>>")
#         quick_sort_algo(arr, pivot_index+1, end)
    



# def quick_sort(arr):
#     quick_sort_algo(arr, 0, len(arr)-1)



def bubble_sort(data):
    flag = True

    while flag:
        flag = False

        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag = True

    data.reverse()

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
bubble_sort(arr_sorted)
bubble_sort(bravery_scores)
    
for i in arr_sorted:
    arr_dic[i].sort()
 
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