#https://docs.google.com/document/d/1bLo4d3MQmqRY1lKC1HNeY22EU06lAecXd2JInJGLIlk/edit
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)

        for x in nums:
            count[x]+=1
        #list of lists, basically buckets
        freq = [[] for i in range(len(nums)+1)]
        #print(freq)
        #freq: 0 1 2 3 4 5 6
        #        3 2 1
        for v,f in count.items():
            #print(v,f)
            #freq[]
            freq[f].append(v)
        #print(freq)
        i = 0
        res = []
        for i in range(len(freq)-1,0,-1):
    
            for j in freq[i]:
                
              if(len(res) < k):  
                    res.append(j)
        
        return res

