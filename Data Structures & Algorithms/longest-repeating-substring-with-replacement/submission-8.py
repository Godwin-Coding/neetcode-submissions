class Solution:
    def characterReplacement(self, s, k):
        freq = {}
        l, r = 0,0
        k1 = k
        res = 0
        while r < len(s): #O(n) time

            if k1 >= 0:
                freq[s[r]] = freq.get(s[r], 0) + 1
            
            win_len = r-l+1
            #O(k) time, where k is the number of unique elements in the dict. finds the number of slots the
            #most freq ocurring number takes up in the window
            mf = freq[max(freq, key=freq.get)]
            k1 = k - (win_len - mf)
            print("NEW LOOP NEW k", k1)
            
            if k1 >= 0:
                res = max(res, win_len)
                
                print("------- new res --------- ")
                for i in range(l, r+1):
                    print(s[i])
                print("------- END --------- ")

                r += 1

                
            elif k1 < 0:
                print("*********** window shortening bc k is:", k1)
                freq[s[l]] = freq.get(s[l], 0) - 1
                l += 1

        return res
            
            
             

#BBABAAACC