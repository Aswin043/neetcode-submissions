class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        window = 0
        max_freq = 0

        for right in range(len(s)):
            freq[s[right]]=1+freq.get(s[right],0)
            max_freq = max(max_freq,freq[s[right]])

            while (right - left +1) - max_freq > k:
                freq[s[left]] -=1
                left +=1
            
            window = max(window,right-left +1)
        return window