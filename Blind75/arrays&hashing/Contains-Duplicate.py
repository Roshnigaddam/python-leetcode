
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      
      
        count = defaultdict(int)
        for x in nums:
           count[x] += 1

        for val in count.values():
            if val > 1:
                return True
            
        return False


#
# Time complexity: O(n).
# We do search() and insert() for n times and each operation takes constant time.

# Space complexity: O(n).
# The space used by a hash table is linear with the number of elements in it.
