class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        
        ptr1 = 0
        ptr2 = 1
        _min = float('-inf')

        while ptr1 < len(arr):
            if ptr2 < len(arr):
                if _min < arr[ptr2]:
                    arr[ptr1] = arr[ptr2]
                    _min = arr[ptr2]
                ptr2 += 1
            else:
                ptr1 += 1
                ptr2 = ptr1 + 1
                _min = float('-inf')
        
        arr[-1] = -1
        return arr