class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for bk in s:
            if ( bk == ')' or bk == '}' or bk == ']' ) and len(res) == 0:
                return False
            elif bk == ')':
                if res[-1] != '(':
                    return False
                res.pop()
            elif bk == ']':
                if res[-1] != '[':
                    return False
                res.pop()
            elif bk == '}':
                if res[-1] != '{':
                    return False
                res.pop()
            else:
                res.append(bk)
        if len(res) != 0:
            return False
        return True