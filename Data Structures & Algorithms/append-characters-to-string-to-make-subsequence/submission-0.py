class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        index=0
        for ch in s:
            if index<len(t) and ch==t[index]:
                index+=1
        return len(t)-index

        