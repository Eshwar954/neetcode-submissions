class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        word=s.split(" ")
        result=len(word[-1])
        return result