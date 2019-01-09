#practice wiht for loop
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        sSplit = S.split()
        
        jSplit = J.split()
        
        count = 0
        
        for letter  in sSplit:
                        
            if letter in jSplit:
                count += 1
                
                
        return count


# or use a set

def numJewelsInStones(self, J, S):
        # runtime: 39ms
        Jset, count = set(J), 0
        for i in S:
            if i in Jset:
                count+=1
        return count
                
                
                
        
            
            
         