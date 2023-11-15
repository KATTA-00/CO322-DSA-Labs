import matplotlib.pyplot as plt

# Data for plotting
array_sizes = [10, 20, 100, 150, 1000, 10000, 100000]

# Best-Case Data
bubble_sort_best = [10400, 4200, 10400, 9400, 81700, 756600, 5292100]
selection_sort_best = [24100, 21100, 303400, 581500, 9396100, 55137100, 1534489800]
insertion_sort_best = [19100, 3700, 10600, 15900, 95900, 880600, 3406600]

# Worst-Case Data
bubble_sort_worst = [12800, 16800, 135900, 208800, 4338300, 100810000, 9794596700]
selection_sort_worst = [100000, 14700, 255100, 109800, 2797200, 38245400, 4266750900]
insertion_sort_worst = [14500, 11000, 86400, 145500, 1338600, 64721300, 6504190400]

# Average-Case Data
bubble_sort_avg = [1300, 2800, 37600, 112300, 2615300, 198475800, 19118995400]
selection_sort_avg = [2000, 2400, 14100, 27000, 427700, 48429500, 1614373600]
insertion_sort_avg = [800, 1600, 9900, 27100, 897600, 48365000, 3588064000]

# Calculate averages for each array size
avg_bubble_sort = [(best + worst + avg) / 3 for best, worst, avg in zip(bubble_sort_best, bubble_sort_worst, bubble_sort_avg)]
avg_selection_sort = [(best + worst + avg) / 3 for best, worst, avg in zip(selection_sort_best, selection_sort_worst, selection_sort_avg)]
avg_insertion_sort = [(best + worst + avg) / 3 for best, worst, avg in zip(insertion_sort_best, insertion_sort_worst, insertion_sort_avg)]

# Plotting
# plt.figure(figsize=(10, 6))

# Average Plot
plt.plot(array_sizes, avg_bubble_sort, label='Bubble Sort (Average)', marker='o')
plt.plot(array_sizes, avg_selection_sort, label='Selection Sort (Average)', marker='o')
plt.plot(array_sizes, avg_insertion_sort, label='Insertion Sort (Average)', marker='o')

plt.xlabel('Array Size')
plt.ylabel('Average Time Complexity (ns)')
plt.title('Sorting Algorithm Averaging Three Cases')

plt.xscale('log')  # Use log scale for better visualization on large datasets
plt.yscale('log')  # Use log scale for better visualization on large datasets


plt.legend()
plt.grid(True)
plt.show()
