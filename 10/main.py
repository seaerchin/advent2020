from collections import defaultdict

def chained(ls, diff = 3): 
    cur = 0
    ls = sorted(ls, key = lambda x: -x) # sort by reverse so when we pop smallest is at back 
    ls = [ls[0] + 3] + ls
    res = [cur]
    while ls and ls[-1] - cur <= diff:
        cur = ls.pop()
        res.append(cur)
    return res

def get_diffs(ls): 
    dp = defaultdict(int)
    for k, v in enumerate(ls[1:], 1): 
        diff = v - ls[k-1]
        dp[diff] += 1 
    return dp

if __name__ == "__main__":
    with open("data.txt", "r") as f:
        input = list(map(int, f.read().splitlines()))
        ls = chained(input)
        dp = get_diffs(ls)
        print(dp[3] * dp[1])