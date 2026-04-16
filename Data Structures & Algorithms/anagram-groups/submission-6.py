class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        sort = ["".join(sorted(e)) for e in strs]
        for e in sort:
            d[e] = list()
        for i in strs:
            d["".join(sorted(i))].append(i)
        return list(d.values())