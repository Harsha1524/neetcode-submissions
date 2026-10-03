class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output=[0]*k
        hashmap= [0]*2001
        for i in nums:
            if i<0:
                i=1000-i
            hashmap[i]+=1
        
        for j in range(k):
            temp=0
            for i in range(2001):
                if hashmap[i]>temp:
                    temp = hashmap[i]
                    if i <=1000:
                        output[j]=i
                    else:
                        output[j]=1000-i
            if output[j]>=0:
                hashmap[output[j]]=0
            else:
                hashmap[1000-output[j]]=0
        return output


        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)

        # for n, c in count.items():
        #     freq[c].append(n)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res