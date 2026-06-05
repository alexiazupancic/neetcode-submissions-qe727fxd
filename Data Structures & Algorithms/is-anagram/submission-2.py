class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       s_set = set([x for x in s])
       t_set = set([x for x in t])
       
       if t_set == s_set:
          return True
       else:
          return False
     
        


        