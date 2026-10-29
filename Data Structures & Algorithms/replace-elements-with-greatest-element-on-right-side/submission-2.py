class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        
        current_max = arr[-1]
        

        for i in range(len(arr)-2, -1, -1):
            current_data = arr[i]
            arr[i] = current_max
            if current_data > current_max:
                current_max = current_data

        arr[-1] = -1
        return arr