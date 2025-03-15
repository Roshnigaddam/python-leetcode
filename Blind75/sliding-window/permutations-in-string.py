class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len_s1 = len(s1)
        len_s2 = len(s2)

        freq1 = {}
        for s in s1:
            freq1[s] = freq1.get(s,0) + 1
        
        window = {}

        if len_s1 > len_s2:
            return False
        #we are running this window over s1 of size len_s1
        for i in range(len_s1):
            c = s2[i]
            window[c] = window.get(c,0) + 1

        #now if window of size len_s1 and freq are same then
        #return true

        if window == freq1: 
            return True

        for i in range(len_s1, len_s2):
            #character leaving the window
            left_char = s2[i - len_s1]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            right_char = s2[i]
            window[right_char] = window.get(right_char,0) + 1

            if window == freq1:
                return True
        return False
            
