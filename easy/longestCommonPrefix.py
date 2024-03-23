# Runtime
# 16
# ms
# Beats
# 61.82%
# of users with Python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pstr = ""
        if len(strs)>=200 or len(strs)<=1:
            if len(strs)==1:
                return strs[0]
            return ""
        p = [len(x) for x in strs]
        for j in range(min(p)):
            flag = False
            for i in range(len(strs)):
                if strs[0][j] != strs[i][j]:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                pstr +=strs[0][j]
            else:
                break

        return pstr


            