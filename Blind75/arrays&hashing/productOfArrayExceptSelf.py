class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        # if 
        # prod = [nums[0:i]*nums[i+1:len(nums)] for i in range(len(nums))]
        # print(prod)
        # for i in range(len(nums)):
        #     res[i] = nums[0:i]*nums[i+1:len(nums)]
            
        # print(res)
        #print(nums[i+1:len(nums)])
        sum=1
        i=0
        # while(i<len(nums)):
        #     for i in nums[0:i].append(nums[i+1:len(nums)-1]):
        #         sum=sum*i
        #     i+=1
        # print(sum)

        #print(nums[0:i].append(nums[i:len(nums)-1]))
        #l=nums[0:i]+(nums[i+1:len(nums)])
        #print(l)
        prod=[]
        while(i<len(nums)):
            for j in nums[0:i]+(nums[i+1:len(nums)]):
                
                sum=sum*j
                #print(i,j,sum)
            i+=1
            prod.append(sum)
            sum=1
        return prod
