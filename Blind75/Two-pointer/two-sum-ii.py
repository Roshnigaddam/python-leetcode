class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        print(l,r)
        cur_sum=0
        print(numbers[1])
        while(l < r):
            cur_sum = numbers[l]+numbers[r]
            if cur_sum == target:
                return [l+1,r+1]
            elif cur_sum > target:
                r-=1
            else:
                l+=1
