def makeChange(n, denom):
    # print(n, denom)

    # print(n, denom)
    if n < 0:
        # print("->", 0)
        return 0

    if denom == 1:
        if n < 3:
            # print("->", n, denom, 1)
            return 1
        else:
            # print("->", n, denom,  0)
            return 0

    next_denom = denom >> 1

    n_ways = 0
    for i in [0, 1, 2]:
        n_ways += makeChange(n-i*denom, next_denom)

    # print("->", n, denom, n_ways)
    return n_ways

n = 10
denom = 1
while (denom <= n):
    denom = denom << 1
denom = denom >> 1

print(makeChange(n, denom))