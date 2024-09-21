class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_map = {}
        
        for i in range(len(nums)):
            num_map[nums[i]] = i
        print(num_map)
        for i in range(len(nums)):
             complement = target - nums[i]
             if complement in nums and num_map[complement]!=i:
                 return [i,num_map[complement]]
                 
# an important note:
# dictionary/hashmap/hashset keys cannot be duplicate

# In Python, a dictionary is a collection of key-value pairs where each key must be unique. 
# If you try to add a duplicate key to a dictionary, the value associated with that key will be updated to the new value, effectively overwriting the previous one

# my_dict = {'a': 1, 'b': 2, 'a': 3}
# print(my_dict)
# {'a': 3, 'b': 2}


# so when nums = [5,5] and given that there is only 1 solution 
# nums_map would be -> {3:1}
