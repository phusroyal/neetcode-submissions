class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_ord = {}
        answer = []
        for s in strs:
            s_ord = self._sum_ord(s)
            
            if s_ord not in str_ord:
                str_ord[s_ord] = len(answer)
                answer.append([s])
            else:
                answer[str_ord[s_ord]].append(s)
        
        return answer

    def _sum_ord(self, strs:str) -> tuple:
        sig = [0]*26
        for x in strs:
            sig[ord(x)-ord('a')] += 1
        return tuple(sig)
