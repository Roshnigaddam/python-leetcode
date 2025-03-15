#Setting max_sum = float('-inf') (negative infinity) is a common technique in algorithms to handle edge cases and ensure that any possible value in the input array will be larger than the initial value.
#float('-inf') represents the smallest possible value in Python — essentially "negative infinity."

def maxSubArray(nums):
    max_sum = float('-inf')
    current_sum = 0
    
    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
      #If current_sum becomes negative, reset it to zero (because a negative sum will reduce future sums)
        if current_sum < 0:
            current_sum = 0
    
    return max_sum

