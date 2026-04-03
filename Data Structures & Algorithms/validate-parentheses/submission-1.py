class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic_pair={
            "]":'[',
            "}":'{',
            ")":'('
        }
        for i in s:
            if i in dic_pair:
                if stack:  
                    if dic_pair[i]!=stack[-1]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            print(stack)
        return not bool(stack)
            