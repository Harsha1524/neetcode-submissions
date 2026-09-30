class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[]
        for i in range(len(s)):
            a.append(ord(s[i]))
        a.sort()
        b=[]
        for i in range(len(t)):
            b.append(ord(t[i]))
        b.sort()
        if a==b:
            return True
        else:
            return False