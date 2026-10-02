class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # output=[]
        # for s in strs:
        #     temp=[]
        #     for t in strs:
        #         if sorted(s) == sorted(t):
        #             temp.append(t)
        #     for t in temp:
        #         if s!= t:
        #             strs.remove(t)
        #     output.append(temp)
        # return output

        
        res = defaultdict(list)

        for s in strs:
            count=[0]*26

            for c in s:
                count[ord(c)-ord('a')] += 1

            res[tuple(count)].append(s)

        return list(res.values())


