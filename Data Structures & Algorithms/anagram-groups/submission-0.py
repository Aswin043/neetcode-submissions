class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs:
            sortedI = ''.join(sorted(i))
            anagrams[sortedI].append(i)
        return list(anagrams.values())

