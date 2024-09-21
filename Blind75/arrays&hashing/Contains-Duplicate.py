
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      
      
        count = defaultdict(int)
        for x in nums:
           count[x] += 1

        for val in count.values():
            if val > 1:
                return True
            
        return False
