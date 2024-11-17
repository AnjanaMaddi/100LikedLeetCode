class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        d = {}
        count = 0
        while p2 >= p1 and p2<len(s):
            if d.get(s[p2],p1-1) < p1:
                d[s[p2]] = p2
                count = max(p2-p1+1, count)
                p2 += 1
            else:
                p1 = d[s[p2]] + 1
        return count
        
