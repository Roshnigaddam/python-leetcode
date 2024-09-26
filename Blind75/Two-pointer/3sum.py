class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums=sorted(nums)
        for i,val in enumerate(nums):
            #print(i,val)
        #print(len(nums)-1)
            if(i>0 and val==nums[i-1]):
                continue

            l,r=i+1,len(nums)-1
            #print(l,r)
            sum = 0 
            while(l<r):
                sum = val + nums[l] + nums[r]
                #print(sum)
                if sum < 0:
                    l+=1
                elif sum > 0:
                    r-=1
                else:
                    res.append([val,nums[l],nums[r]])
                    l+=1
                    
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


#######explaination:######
#we basically fix one element, so that res of the problem will be a 2sum
