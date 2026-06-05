class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [x for x in s]
        t_list = [x for x in t]

        common = []
        for s_item in s_list:
            if s_item in t_list:
                common.append(s_item)

        
        if len(common) == len(s_list) == len(t_list):
            return True
        else:
            return False
        


        