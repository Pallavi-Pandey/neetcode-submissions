class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t) 
        # it gives the frquency of the string, 
        # count.most_common(2) to get the top most common elements