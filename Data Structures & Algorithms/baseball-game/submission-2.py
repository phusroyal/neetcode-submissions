class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for op in operations:
            print(res)
            if op == '+':
                res.append(res[-1]+res[-2])
            elif op == 'C':
                res.pop()
            elif op == 'D':
                res.append(res[-1]*2)
            else:
                res.append(int(op))
        
        return sum(res)


    def _checkInt(self, num_str: str) -> bool:
        if num_str[0] == '-':
            return num_str[0:].isnumeric()
        return num_str.isnumeric()