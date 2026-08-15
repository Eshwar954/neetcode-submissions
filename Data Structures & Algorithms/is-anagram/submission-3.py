class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        left=0
        right=len(s)-1
        freq={}
        if len(s)!=len(t):
            return False
        for char in s:
            freq[char]=freq.get(char,0)+1
        for char in t:
            if char in freq:
                freq[char]=freq.get(char,0)-1
        for value in freq.values():
            if value>0:
                return False        
        return True