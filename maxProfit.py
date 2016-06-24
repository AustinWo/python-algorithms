day1Prices = [5,4,3,2,1]
day2Prices = [1,2,3,4,5]

def getMaxProfit(prices):
    if len(prices) < 2:
        raise IndexError('must have more than 2 prices')
    minPrice = min(prices[0], prices[1])
    maxProfit = prices[1]-prices[0]
    
    for index in range(2, len(prices)):
        currentPrice = prices[index]
        potentialProfit = currentPrice - minPrice
        maxProfit = max(maxProfit, potentialProfit)
        minPrice = min(minPrice, currentPrice)
    return maxProfit

print(getMaxProfit(day1Prices))
print(getMaxProfit(day2Prices))