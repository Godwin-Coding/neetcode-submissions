class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        want = {}
        for c in s1:
            want[c] = want.get(c, 0) + 1

        have = {}
        matches = 0
        l = 0

        for r in range(len(s2)):
            c = s2[r]
            have[c] = have.get(c, 0) + 1
            if c in want and have[c] == want[c]:
                matches += 1

            if r - l + 1 > len(s1):  # shrink to fixed size
                left = s2[l]
                if left in want and have[left] == want[left]:
                    matches -= 1
                have[left] -= 1
                l += 1

            if matches == len(want):
                return True

        return False