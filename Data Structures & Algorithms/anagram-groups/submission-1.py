class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for i in strs:
            key=''.join(sorted(i))
            dic[key].append(i)
        return list(dic.values())