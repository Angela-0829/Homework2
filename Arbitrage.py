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

from itertools import permutations
all_path = list(permutations(["tokenA", "tokenC", "tokenD", "tokenE"], 4))
max_amount = 0
for i in range(len(all_path)):
    current_path = ["tokenB"]
    current_path.extend(list(all_path[i]))
    current_path.append("tokenB")
    current_amount = getBalance(current_path, 5)
    if current_amount > max_amount:
        max_amount = current_amount
        best_path = current_path
print("path:", "->".join(token for token in best_path) + ", tokenB balance=" + str(getBalance(best_path, 5)))


