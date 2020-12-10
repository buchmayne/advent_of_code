f = open("input_data.txt", "r")
data = f.read()
data = data.split("\n")
data = [int(x) for x in data]
data = sorted(data)

jolts = 0
one_jolt_diff = 0
three_jolt_diff = 1

for i in list(range(len(data))):
    diff_ = data[i] - jolts
    if diff_ == 1:
        one_jolt_diff += 1
    if diff_ == 3:
        three_jolt_diff += 1
    jolts = data[i]

part1_answer = one_jolt_diff * three_jolt_diff

# Part 2 // dynamic programming (thanks youtube)
DP = {}
data.append(max(data) + 3)
data.append(0)
data = sorted(data)


def dp(i):
    if i == (len(data) - 1):
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i + 1, len(data)):
        if data[j] - data[i] <= 3:
            ans += dp(j)
    DP[i] = ans
    return ans


print(dp(0))