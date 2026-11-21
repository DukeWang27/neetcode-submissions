from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) #the default value is an empty list
        result = []
        #i know if i sort and compare then it would be easily able to distinguish if its an anagram
        #however then i would need to return a list in the end but also use a hashmap
        for s in strs:
            sorted_s = tuple(sorted(s))
            hashMap[sorted_s].append(s)
        
        for value in hashMap.values():
            result.append(value)
        
        return result