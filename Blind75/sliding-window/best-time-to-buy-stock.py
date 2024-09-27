class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        temp=0
        maxp=0

        while(r<len(prices) ):
            print(l,r,prices[l],prices[r])
            
            if(prices[l] <= prices[r]):
                temp = prices[r] - prices[l]
                maxp=max(temp,maxp)
                
            else:
                l=r
            r+=1
    
        return(maxp)

  ###keep updating left pointer to lowest price
