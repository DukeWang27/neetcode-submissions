class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + "#" + word
        return res
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length #we do this since lets say for example 
            #what we did in the previous lines of code
            #we string sliced to only get the word and we found out how long each word is since we did length = int(str[i:j]) im still a bit confused on why we did [i:j] but oh wait its because we have to user varaibles since there are several words and to update make it save continuity.
        return res


