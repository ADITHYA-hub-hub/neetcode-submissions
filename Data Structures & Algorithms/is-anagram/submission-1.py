class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana_1={}
        ana_2={}

        if(len(s)!=len(t)):
            return False
        
        for i in range(len(s)):
            ana_1[s[i]]=ana_1.get(s[i],0)+1
            ana_2[t[i]]=ana_2.get(t[i],0)+1
        
        if ana_1==ana_2:
            return True
        return False