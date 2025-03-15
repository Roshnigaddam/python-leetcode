class Solution:
    def isValid(self, s: str) -> bool:
        
        #what will you search with? you will search a corresponding open bracket 
        #for a closed bracket
        
        hashmap={')':'(','}':'{',']':'['}
        stack=[]
        
        for i in range(0,len(s),1):
           if s[i] in ['(','[','{']:
               
               stack.append(s[i])
               
           if s[i] in [')',']','}']:
               
            
               if len(stack)==0:
                   return False
               if hashmap[s[i]] != stack[-1] :
                   return False
               stack.pop()
           #print(stack)
      
        print("stack:",stack)
        if (len(stack)==0):
           return True
        else:
           return False
      
