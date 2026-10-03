class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for i in range(len(strs)):
            encoded_string+= strs[i]
            encoded_string+= "`"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_string=[]
        temp=""
        for i in s:
            if i != "`":
                temp+= i
            else:
                decoded_string.append(temp)
                temp = ""
        return decoded_string