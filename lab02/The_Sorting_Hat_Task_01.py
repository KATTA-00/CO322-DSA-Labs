def bubble_sort(data, reverse=True):
    flag = True

    while flag:
        flag = False

        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag = True
    if reverse:
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
    bubble_sort(arr_dic[i], False)
 
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