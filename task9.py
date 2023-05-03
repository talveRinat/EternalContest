COUPON_COST = 100
INF = float('inf')


def cafe_solution(n, costs):
    while n > 0 and costs[-1] == 0:
        n -= 1
        costs = costs[:-1]

    if n == 0:
        return 0, 0, []

    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    pr = [[(-1, -1)] * (n + 1) for _ in range(n + 1)]

    if costs[0] > COUPON_COST:
        dp[1][0] = costs[0]
        dp[0][1] = costs[0]
        pr[0][1] = (1, 0)
    else:
        dp[0][0] = costs[0]

    for j in range(n):
        for i in range(n):
            if j < n - 1:
                dp_val_1 = dp[i][j] + costs[j + 1]
                if costs[j + 1] > COUPON_COST and i < n - 1:
                    if dp_val_1 < dp[i + 1][j + 1]:
                        dp[i + 1][j + 1] = dp_val_1
                        pr[i + 1][j + 1] = (i, j)
                else:
                    if dp_val_1 < dp[i][j + 1]:
                        dp[i][j + 1] = dp_val_1
                        pr[i][j + 1] = (i, j)

                if i > 0:
                    dp_val_2 = dp[i][j]
                    if dp_val_2 < dp[i - 1][j + 1]:
                        dp[i - 1][j + 1] = dp_val_2
                        pr[i - 1][j + 1] = (i, j)

    min_cost_sum = INF
    coupons_left = 0
    for i in range(n, -1, -1):
        if min_cost_sum > dp[i][n - 1]:
            min_cost_sum = dp[i][n - 1]
            coupons_left = i

    coupons_lost_days = []
    j = n - 1
    i = coupons_left
    while i > -1 or j > -1:
        pr_i = i
        pr_j = j
        i, j = pr[i][j]
        if i > pr_i:
            coupons_lost_days.append(pr_j + 1)

    return min_cost_sum, coupons_left, coupons_lost_days[::-1]


def main():
    n = int(input())
    costs = []
    for _ in range(n):
        costs.append(int(input()))
    result = cafe_solution(n, costs)
    print(result[0])


if __name__ == "__main__":
    main()
