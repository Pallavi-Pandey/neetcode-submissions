class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            print(f"Encoding string: {s}")
            res += str(len(s)) + "#" + s
        print(f"Encoded string: {res}")
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        print(f"Decoded list: {res}")
            
        return res