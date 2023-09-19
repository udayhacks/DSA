

"""

        
        
        
        
        
        
        
        
        
"""     

from collections import Counter,defaultdict


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: hash map, 
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        freq = defaultdict(bool)
        deletions = 0
        
        for cnt in count.values():
            if freq[cnt]:
                cnt -= 1
                deletions += 1
                while cnt > 0 and freq[cnt]:
                    cnt -= 1
                    deletions += 1
                freq[cnt] = True
            else:
                freq[cnt] = True
                
        return deletions
        
def uday(s):
    cnt = Counter(s)
    frq = defaultdict(bool)
    ans = 0
    for i in cnt.values ():
        if frq[i] :
            i-=1
            ans+=1
            while i > 0 and frq[i] :
                i -=1
                ans+=1
            frq[i]  = True 
        else :
            frq[i] = True 
    return ans 



print(defaultdict(bool))

             
        
        
        
        
        
        
s= "aaabbbcc"   
        
a = Solution()
a.minDeletions(s)