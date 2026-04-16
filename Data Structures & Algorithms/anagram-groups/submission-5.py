class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        ans, copy = [], strs.copy()
        for e in copy:
            if e in strs: #checks that the element hasnt already been included in another sublist
                sublist = [e]
                for j in copy[copy.index(e)+1:]:
                    take = True
                    if e != j:
                        take = False
                        for char in e:
                            if char not in j or e.count(char) != j.count(char) or len(e) != len(j):
                                take = False
                                break
                            take = True
                    if take:
                        sublist.append(j)
                        strs.remove(j)
                strs.remove(e)
                ans += [sublist]
        return ans