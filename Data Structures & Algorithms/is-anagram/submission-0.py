class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen_s = dict()
        seen_t = dict()
        
        for char in s:
            if char not in seen_s:
                seen_s[char] = 0 
            seen_s[char] += 1
            
        for char in t:
            if char not in seen_t:
                seen_t[char] = 0
            seen_t[char] += 1
        #print(seen_s)
        #print(seen_t)
        return seen_s == seen_t