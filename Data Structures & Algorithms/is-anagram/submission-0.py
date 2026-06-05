class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = set(s)
        t1 = set(t)
        if s1.union(t1) == s1.intersection(t1):
            return True
        else:
            return False


        