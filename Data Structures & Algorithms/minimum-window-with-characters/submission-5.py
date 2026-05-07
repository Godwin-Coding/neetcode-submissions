class Solution:
    def minWindow(self, s: str, t: str) -> str:
        to_find = {}
        for letter in t:
            to_find[letter] = to_find.get(letter, 0) + 1
        
        have = {}
        r = 0
        start = 1000
        res = ""
        matches = 0
        for l in range(len(s)):
            
            if s[l] not in to_find:
                continue
            print("curr letter checking:", s[l])
            
            for r in range(l, len(s)):
                if s[r] not in to_find:
                    continue
                start = min(start, r)
                have[s[r]] = have.get(s[r], 0) + 1
                if have[s[r]] == to_find[s[r]]:
                    matches += 1   
                if matches == len(to_find):
                    print("found contender:", s[start:r+1])
                    if res == "":
                        res = s[start:r+1]
                    else:
                        res = s[start:r+1] if len(s[start:r+1]) < len(res) else res
                    r, start, have, matches = 0, 1000, {}, 0
                    print("reset", r, start, have)
                    break
                elif r == len(s) - 1:
                    print("ended")
                    r, start, have, matches = 0, 1000, {}, 0

        return res