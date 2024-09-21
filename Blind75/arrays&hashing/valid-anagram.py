class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        # Count the frequency of characters in string s
        for x in s:
            count_s[x] += 1
        
        for x in t:
            count_t[x] += 1
        
        if count_s==count_t:
            return True
        else:
            return False


#or

class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
       count = defaultdict(int)
      
       # Count the frequency of characters in string s
       for x in s:
           count[x] += 1
      
       # Decrement the frequency of characters in string t
       for x in t:
           count[x] -= 1
      
       # Check if any character has non-zero frequency
       for val in count.values():
           if val != 0:
               return False
      
       return True

