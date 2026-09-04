class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters=set()
        left =0 
        window=0

        for r in range(len(s)):
            while s[r] in letters:
                letters.remove(s[left])
                left+=1
            letters.add(s[r])
            window = max(window, r - left +1)

        return window