class Solution:
    def minWindow(self, s: str, t: str) -> str:
        to_find = {}
        for letter in t:
            to_find[letter] = to_find.get(letter, 0) + 1
        
        have = {}
        l, r = 0, 0
        matches = 0
        res = ""

        while r < len(s):
            if s[r] in to_find:
                have[s[r]] = have.get(s[r], 0) + 1
            if s[r] in have and s[r] in to_find and have[s[r]] == to_find[s[r]]:
                matches += 1

            while matches == len(to_find):
                if res == "" or len(s[l:r+1]) < len(res):
                    res = s[l:r+1]
                    
                l += 1
                print(l-1)
                if s[l-1] not in to_find:
                    continue
                have[s[l-1]] = have.get(s[l-1], 0) - 1
                if have[s[l-1]] < to_find[s[l-1]]:
                    matches -= 1

            r += 1


        return res