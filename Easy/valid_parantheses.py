class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        checker = []
        pop_sample = {'(': ')', '[' : ']', '{' : '}'}
        
        for b in range(len(s)):
            if s[b] in pop_sample.keys():
              checker.append(s[b])
            elif len(checker) == 0 or s[b] != pop_sample[checker.pop()]:
              return False
        if len(checker) == 0:
          return True