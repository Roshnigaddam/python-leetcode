class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        #slist=list(s)
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s)

        l=0
        r=len(cleaned_s) - 1

        while l < r:
            print(cleaned_s[l],cleaned_s[r])
            if cleaned_s[l]!=cleaned_s[r]:
                return False
            
            l=l+1
            r=r-1
        return True
