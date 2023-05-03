n = int(input())
a, b, c = map(int, input().split())

dp = [False] * (n+1)
dp[1] = True

for i in range(2, n+1):
    if i-a >= 1:
        dp[i] = dp[i] | dp[i-a]
    if i-b >= 1:
        dp[i] = dp[i] | dp[i-b]
    if i-c >= 1:
        dp[i] = dp[i] | dp[i-c]

print(sum(dp[1:]))
