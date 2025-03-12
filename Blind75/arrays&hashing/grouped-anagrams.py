#dictionary/hashmap - you are gorouping anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #dictionary key - sorted string value - list of anagrams
        anagram_map = {}

        #for each word in the list:
        for word in strs:
            #sort the characters in the word
            sorted_word = ''.join(sorted(word))

            #if this key does not exist in the map and create a list
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []

            #add the current word to the corresponsing list
            anagram_map[sorted_word].append(word)
        return list(anagram_map.values())
            
