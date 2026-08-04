class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_spd = max(piles)
        res = max_spd
        min_spd = 1
        while max_spd >= min_spd:
            mid_spd = (max_spd + min_spd)//2
            mid_spd = mid_spd + 1 if mid_spd == 0 else mid_spd
            h_spent = 0
            for m in piles:
                h_spent += (m//mid_spd)+1 if (m/mid_spd) % 1 else m//mid_spd

            if h_spent > h:
                min_spd = mid_spd+1

            elif h_spent <= h:
                res = min(res, mid_spd)
                max_spd = mid_spd-1
        return res