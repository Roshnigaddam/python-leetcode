class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        l = 0
        char_map = {}
        max_count = 0
        right = 0
        for right in range(len(s)):

            current_char = s[right]
            char_map[current_char] = char_map.get(current_char,0) + 1
            #ideal window size = most_popular_size + k

            max_count = max(max_count,char_map[current_char]) #most popular candidate
            window_size = right - l + 1

            if window_size - max_count > k: #shrink window
                left_char = s[l]

                char_map[left_char] -=1

                if char_map[left_char] == 0:
                    del char_map[left_char]
                l+=1
            res = right - l +1
            res = max(res,right - l +1)
        return res



