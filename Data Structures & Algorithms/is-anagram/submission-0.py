class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_1=list(s)
        list_2=list(t)
        
        list_1.sort()
        list_2.sort()

        if(list_1==list_2):
            return True
        return False