class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        
        if len(s)!= len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]]= 1+countS.get(s[i],0)
            countT[t[i]]= 1+countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True

        # a=[]
        # for i in range(len(s)):
        #     a.append(ord(s[i]))
        # a.sort()
        # b=[]
        # for i in range(len(t)):
        #     b.append(ord(t[i]))
        # b.sort()
        # if a==b:
        #     return True
        # else:
        #     return False