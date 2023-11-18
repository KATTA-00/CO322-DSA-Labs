n, m = map(int, input().strip().split(" "))

arr1 = list(map(int, input().strip().split(" ")))
arr2 = list(map(int, input().strip().split(" ")))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):

        if arr1[i - 1] == arr2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

longest = []
i = n
j = m
while i > 0 and j > 0:
    if arr1[i - 1] == arr2[j - 1]:
        longest.append(arr1[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] < dp[i][j - 1]:
        j -= 1
    else:
        i -= 1

longest.reverse()
print(" ".join([str(i) for i in longest]))