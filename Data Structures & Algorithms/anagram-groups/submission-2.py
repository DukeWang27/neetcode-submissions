class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {} #empty dictionary
        for word in strs: #we iterate each word over the list
            key = "".join(sorted(word)) #we create a key which is the sorted letters of each word
            if key not in anagram: #this automatically just checks if the dictionary contains the key
                anagram[key] = [word] #if the dictionary does not contain the key then it will create that key value pair with that regular word
            else:
                anagram[key].append(word) #if the anagram that we iterated over is in the anagram then we have to add that specific word to the list of values from that key.
        result = []
        for values in anagram.values():
            result.append(values)
        
        return result
            
        

        
