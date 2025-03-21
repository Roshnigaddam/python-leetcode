class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            #if complemnt and number are same we should be able to return different      indexes Ex: nums = [3,3], target = 6
            if complement in hashmap and i!=hashmap[complement] :
                return [i, hashmap[complement]]
            #so for at this point {3:0} will become {3:1}
            hashmap[nums[i]] = i
        
        return []

#---------------
#time complexity
# Complexity Analysis

# Time complexity: O(n).
# We traverse the list containing n elements only once. Each lookup in the table costs only O(1) time.

# Space complexity: O(n).
# The extra space required depends on the number of items stored in the hash table, which stores at most n elements.

#---------------
# an important note:
# dictionary/hashmap/hashset keys cannot be duplicate

# In Python, a dictionary is a collection of key-value pairs where each key must be unique. 
# If you try to add a duplicate key to a dictionary, the value associated with that key will be updated to the new value, effectively overwriting the previous one

# my_dict = {'a': 1, 'b': 2, 'a': 3}
# print(my_dict)
# {'a': 3, 'b': 2}


# so when nums = [5,5] and given that there is only 1 solution 
# nums_map would be -> {5:1}
