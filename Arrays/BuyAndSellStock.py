class BuyAndSellStock:
    # brute force method
    def maxProfit(self, prices:list[int])-> int:
        max_profit=0
        k=len(prices)
        for i in range(0,k):
            for j in range(i+1, k):
                profit=prices[j]-prices[i]
                if profit>max_profit:
                    max_profit=profit
        
        return max_profit
        
        # optimal solution
    def max_profit_otimal(self,prices:list[int]) -> int:
        min_price=prices[0]
        max_profit=0
        for price in prices:
            if min_price>price:
                min_price=price
            elif (price-min_price)>max_profit:
                max_profit=int(price-min_price)
        return max_profit
            
        
    # test code
        
prices = [7,1,5,3,6,4]#[7,6,4,3,1] #[7,1,5,3,6,4]
obj=BuyAndSellStock()
print(obj.max_profit_otimal(prices=prices))