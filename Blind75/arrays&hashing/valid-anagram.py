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
