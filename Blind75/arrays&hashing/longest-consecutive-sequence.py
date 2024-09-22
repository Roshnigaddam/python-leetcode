#https://docs.google.com/document/d/1jNYE1Db2hnhIvK1Fl_bpjuhZZ-HXJWY2hrUaNveLZXs/edit

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = []
        num_set=set(nums)
        longest_streak=0
        for n in num_set:
          if n-1 not in num_set:
            current_element = n
            current_streak=1
            while current_element+1 in num_set:
                   current_element +=1
                   current_streak += 1
                   #print(current_element)
            longest_streak = max(longest_streak,current_streak)
        return longest_streak

        
