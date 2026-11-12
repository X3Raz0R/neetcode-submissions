class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":      # citim lungimea
                j += 1
            length = int(s[i:j])
            start = j + 1           # sărim peste '#'
            res.append(s[start:start + length])
            i = start + length      # trecem la următorul string
        return res