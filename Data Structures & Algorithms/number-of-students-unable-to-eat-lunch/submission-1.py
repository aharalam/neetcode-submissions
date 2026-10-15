from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # square sandwiches = 0
        # circular sandwiches = 0
        queue = deque(students)
        i = 0
        rotations = 0

        # if the student at the front of the queue prefers the sandwich on the top
        # of the stack, they will take it and leave the queue:

        # Otherwise, they will leave it and go to the queue's end:

        # This continues until none of the queue students want to take the top sandwich and are
        # thus unable to eat.

        while queue and i < len(sandwiches):
            if queue[0] == sandwiches[i]:
                queue.popleft()
                i += 1
                rotations = 0
            else:
                queue.append(queue.popleft())
                rotations += 1

                if rotations == len(queue):
                    break
        
        return len(queue)