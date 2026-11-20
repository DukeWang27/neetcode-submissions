

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        #I think this problem will take O(n) time complexity since we have to actually go throuhg the entirety of the list and see which elements are frequent and the # of elements that are most frequent. 
#In addition i think i need to create a dictionary to store the infromation since that would be easier to retrieve so I think each number should have a corressponding count within the dictionary as the value.
        for value in nums:
            if value not in counts:
                counts[value] = 1
            else:
                counts[value] += 1
        #now that we have everything and its counts within the dictionary. We shoudl display which numbers were the most frequent with the given # of numbers that they asked for. 
    
        #i have an idea so pretty much we need to get the keys from the dictionary sort them then with the sotrting we can index and it would work since we just put whatever k elements wwas within the indexing. Another thing is that if we do this wheere we sort it and put it in a list we have to return that too 
        myList = sorted(counts.keys(), reverse=True, key=counts.get)
        return myList[0:k]
            
