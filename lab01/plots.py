import matplotlib.pyplot as plt

def plot_algorithm(algorithm, sizes, best_case, worst_case, average_case, color):
    plt.plot(sizes, best_case, label='Best Case', color='red', marker="*")
    plt.plot(sizes, worst_case, label='Worst Case', color='green', marker="o")
    plt.plot(sizes, average_case, label='Average Case', color='blue', marker="^")

# Data for Bubble Sort
bubble_sizes = [10, 20, 100, 150, 1000, 10000, 100000]
bubble_best = [10400, 4200, 10400, 9400, 81700, 756600, 5292100]
bubble_worst = [12800, 16800, 135900, 208800, 4338300, 100810000, 9794596700]
bubble_average = [1300, 2800, 37600, 112300, 2615300, 198475800, 19118995400]

# Data for Selection Sort
selection_best = [24100, 21100, 303400, 581500, 9396100, 55137100, 1534489800]
selection_worst = [100000, 14700, 255100, 109800, 2797200, 38245400, 4266750900]
selection_average = [2000, 2400, 14100, 27000, 427700, 48429500, 1614373600]

# Data for Insertion Sort
insertion_best = [19100, 3700, 10600, 15900, 95900, 880600, 3406600]
insertion_worst = [14500, 11000, 86400, 145500, 1338600, 64721300, 6504190400]
insertion_average = [800, 1600, 9900, 27100, 897600, 48365000, 3588064000]

# Plotting
# plt.figure(figsize=(12, 8))

# algo__name = "Bubble"
# algo__name = "Selection"
algo__name = "Insertion"

# plot_algorithm('Bubble Sort', bubble_sizes, bubble_best, bubble_worst, bubble_average, 'red')
# plot_algorithm('Selection Sort', bubble_sizes, selection_best, selection_worst, selection_average, 'green')
plot_algorithm('Insertion Sort', bubble_sizes, insertion_best, insertion_worst, insertion_average, 'blue')

plt.xlabel('Array Size')
plt.ylabel('Time (ns)')

plt.title(algo__name + " Sort Algorithm Performance - log scale")

plt.legend()

plt.xscale('log')  # Use log scale for better visualization on large datasets
plt.yscale('log')  # Use log scale for better visualization on large datasets

plt.grid(True)

plt.show()
