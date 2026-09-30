class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
            
        return list(groups.values())
        
        # nested_list = []
        # temp = []
        # while len(strs)!=0:
        #     temp.append(strs[0])
        #     for i in range(len(strs)):
        #         if Counter(strs[i]) == Counter(strs[0]):
        #             temp.append(strs[i])
        #     for i in range(len(temp)):
        #         strs.remove(temp[i])
        # nested_list.append(temp)
        # return nested_list
       


