class Solution:
    def maxArea(self, height: List[int]) -> int:
            i=1
       
            l,r = 0, len(height)-1
            
               
            area = 0
            
            temp=0
            while(l<r):
                temp = (r-l)*(min(height[l],height[r]))
                
                area = max(temp,area)
                #print(l,r,height[l],height[r],area)
                if(height[l]<height[r]):
                    l+=1
                
                else:
                    r=r-1

            #print(l,r,height[l],height[r])
            return area
