class Solution:
    def isPalindrome(self, s: str) -> bool:
        req=""
        for l in s:
            if l.isalnum():
                req+=l
        a=req.lower()

        left=0
        right=len(a)-1

        while left<right:
            if a[left]!=a[right]:
                return False
            left+=1
            right-=1
        return True
