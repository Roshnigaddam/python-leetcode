approach 1 : brute force: xxxxx - error - array index out of bounds:

code was:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        list1 = []
        list1.append([strs[0]])
        print(list1)
        for i in range(len(strs)):


            j=i+1
            list1.append([strs[i]])     #------error IndexError: list index out of range
            while(j < len(strs)):
                if(self.isAnagram(strs[i],strs[j])):
                    list1[i].append(strs[j])
                    strs.remove(strs[j])
                j+=1
        return list1

    def isAnagram(self, str1: str, str2: str) -> bool:
        count = defaultdict(int)
        for x in str1:
            count[x]+=1
        for x in str2:
            count[x]-=1
        
        for val in count.values():
            if val > 0:
                return False

        return True

#error explaination : when I am removing elements from list, so when i am trying to append at index it is out of range

#correction by adding flags for grouped elements instead of removing elements grouped

