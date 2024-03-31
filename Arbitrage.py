liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}
token = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]
token_id = {"tokenA": 0, "tokenB": 1, "tokenC": 2, "tokenD": 3, "tokenE": 4}

def getAmountIn(tokenIn, tokenOut, amountOut):
    if token_id[tokenIn] < token_id[tokenOut]:
        liquid = liquidity[(tokenIn, tokenOut)]
        tokenIn01 = 0
        tokenOut01 = 1
    else:
        liquid = liquidity[(tokenOut, tokenIn)]
        tokenIn01 = 1
        tokenOut01 = 0
    amount = (liquid[tokenIn01] * amountOut * 1000) / ((liquid[tokenOut01] - amountOut) * 997) + 1
    return amount

def getAmountOut(tokenIn, tokenOut, amountIn):
    if token_id[tokenIn] < token_id[tokenOut]:
        liquid = liquidity[(tokenIn, tokenOut)]
        tokenIn01 = 0
        tokenOut01 = 1
    else:
        liquid = liquidity[(tokenOut, tokenIn)]
        tokenIn01 = 1
        tokenOut01 = 0
    amount = 997 * amountIn * liquid[tokenOut01] / (1000 * liquid[tokenIn01] + 997 * amountIn)
    return amount

def getBalance(path, amountIn):
    for i in range(len(path)-1):
        tokenIn = path[i]
        tokenOut = path[i+1]
        amountOut = getAmountOut(tokenIn, tokenOut, amountIn)
        # print(amountOut)
        amountIn = amountOut
    return amountOut

target = "tokenB"
path = [target]
while len(path) <= 5:
    tokenOut = path[-1]
    amountMin = 9999
    for i in range(len(token)):
        if i == token_id[tokenOut]:
            continue
        amount = getAmountIn(token[i], tokenOut, 1)
        if amount < amountMin:
            amountMin = amount
            tokenMin = i
    path.append(token[tokenMin])

path.reverse()
path.insert(0, target)
print("path:", "->".join(token for token in path) + ", tokenB balance=" + str(getBalance(path, 5)))

    



