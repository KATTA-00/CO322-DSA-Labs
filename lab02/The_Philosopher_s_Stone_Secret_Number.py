t = int(input())

dp = [-1] * 987
dp[0] = 1
dp[1] = 1

count = 1                

def getFib(num):
    if count >= num:
        return dp[num-1]

    for i in range(count+1, num):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[num-1]


for _ in range(t):
    num = int(input())

    print(getFib(getFib(num)))

    