
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    checker = []
    last = None
    sample = ['(', '[','{']
    pop_sample = {')': '(', ']' : '[', '}' : '{'}

    if len(s) < 1 or len(s)%2 != 0 or s[0]in pop_sample:
        return False
    else:
        
        for x,i in enumerate(s):
            print(x, i, len(s)-1, len(checker), last)
            print(checker)
            print( x == len(s)-1, len(checker) == 0)


            if i in sample:
                last = i
                checker.append(i)

            elif i in pop_sample.keys():
                if len(checker) != 0 and (pop_sample[i] == last or checker[-1] == pop_sample[i]):
                  # print(checker.pop(), end = ' mmmm.  ')
                  # print(len(checker))
                  checker.pop()
                else:
                  return False
            if x == len(s)-1 and len(checker) == 0:
              return True
        
            

        return False
isValid("[(({})}]")