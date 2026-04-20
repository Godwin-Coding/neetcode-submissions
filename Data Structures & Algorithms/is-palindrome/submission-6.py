class Solution:
    def isPalindrome(self, s):
        s = s.replace(" ", "").lower()
        st = ""
        for let in s:
            if ord('a') <= ord(let) <= ord('z') or ord("0") <= ord(let) <= ord('9'):
                st += let
        if len(st) % 2 == 0:
            l, r = st[:(len(st)//2)], st[(len(st)//2):]
        else:
            l, r = st[:(len(st)//2)], st[len(st)//2+1:]
        if l == r[::-1]:
            return True
        return False
