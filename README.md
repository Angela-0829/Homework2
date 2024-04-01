# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution  
path: tokenB->tokenA->tokenE->tokenD->tokenC->tokenB  
swap1: tokenB->tokenA, amountIn=5, amountOut=5.655321988655322  
swap2: tokenA->tokenE, amountIn=5.655321988655322, amountOut=1.0583153138066885  
swap3: tokenE->tokenD, amountIn=1.0583153138066885, amountOut=2.429786260142227  
swap4: tokenD->tokenC, amountIn=2.429786260142227, amountOut=5.038996197252911  
swap5: tokenC->tokenB, amountIn=5.038996197252911, amountOut=20.042339589188174  
final reward=20.042339589188174

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution  
可能會因為AMM市場波動，導致交易進行時預期價格和實際價格不一樣，這個差距就是slippage。以addLiquidity這個function為例，參數amountAMin是最少要投入tokenA的數量、amountBMin是最少要投入tokenB的數量。會先使用quote這個函式計算出amountAOptimal和amountBOptimal的數量，若amountAOptimal小於amountAMin或amountBOptimal小於amountBMin，就要revert，即可緩解slippage的問題。


## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution  
這是因為在提供流動性時，流動性池中的初始流動性要夠大，才能保證交易的有效性和穩定性。如果流動性池中的流動性量過小，可能會導致交易時的價格滑動過大，甚至造成流動性降低或市場操縱的問題。因此要扣除最小流動性，才可以確保流動性池中的初始流動性量達到一個合適的水平，減少因流動性不足而導致的交易問題。

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution  
流動性要通過一個公式來獲得，這是因為要盡可能地讓tokens的比例保持相同，以及確保流動性提供者能夠按比例獲得流動性，才能維持流動性池的平衡。

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution  
在我要進行swap時，攻擊者知道token的價格會提高，因此搶先在我之前進行swap，先把token價格提高，此時我進行swap，導致我實際獲得的token數量比預期的少，且又會把價格提得更高，攻擊者再賣出原本買入的token即可賺取價差。

