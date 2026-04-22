class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        window can be safely fixed at len(s1)
        move rightward and see if each letter in window matches that of s1
        if so, immediately return true
        at the end return false
        '''
        want = {}
        have = {}
        for let in s1:
            want[let] = want.get(let, 0) + 1

        
        for r in range(len(s1)-1, len(s2)):
            l = r - (len(s1)-1)
            if l > 0 and s2[l] == s2[l-1] and s2[r] == s2[r-1]:
                #print("condition:", l > 0 and s2[l] == s2[l-1])
                continue



##            print("--------new window from", l, "to", r, "------")
##            for i in range(l, r+1):
##                print(s2[i])

            
            while l <= r:
                have[s2[l]] = have.get(s2[l], 0) + 1
                
                if s2[l] not in want or have[s2[l]] > want[s2[l]]:
                    have = {}
                    break
       
                #print("window has", s2[l], "hence have:", have)

                l += 1
                if l > r:
                    return True

        return False
        