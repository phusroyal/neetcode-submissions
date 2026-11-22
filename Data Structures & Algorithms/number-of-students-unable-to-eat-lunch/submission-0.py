from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        flag = 0
        students = deque(students)
        sandwiches = deque(sandwiches)

        while flag < len(sandwiches):
            st = students.popleft()
            if st == sandwiches[0]:
                sandwiches.popleft()
                flag = 0
            else:
                students.append(st)
                flag += 1 

        return len(students)