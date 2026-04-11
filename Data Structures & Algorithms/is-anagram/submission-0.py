class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        sMap = {}
        tMap = {}

        for i in s:
            sMap[i] = sMap.get(i,0) + 1
        
        for j in t:
            tMap[j] = tMap.get(j,0) + 1


        for i in sMap:
            if i in tMap.keys():
                if sMap[i] != tMap[i]:
                    return False
            else:
                return False
        
        return True
        


        