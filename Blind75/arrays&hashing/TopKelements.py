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
####or use min heap

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
    #use a hashmap to store the elements and the frquesncies

        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1

        #use a min-heap, push ( freq, number ) onto the min heap and we will pop the root 
        #if incoming elements frequency is higher

        min_heap = []

        for num, freq in freq_map.items():
            heapq.heappush(min_heap,(freq,num))
            if(len(min_heap) > k):
                heapq.heappop(min_heap)


        return [num for (freq,num) in min_heap]
