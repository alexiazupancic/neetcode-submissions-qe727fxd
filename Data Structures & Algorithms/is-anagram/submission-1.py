class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = set(s)
        if s1.union(set(t)) == s1.intersection(set(t)) and len(list(s)) == len(list(t)):
            return True
        else:
            return False


        