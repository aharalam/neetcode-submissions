class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        stack = deque(sandwiches)

        while queue and stack:
            if queue[0] == stack[0]:
                queue.popleft()
                stack.popleft()
            elif stack[0] not in queue: # nobody left wants the top
                break
            else:
                queue.append(queue.popleft())
        
        return len(queue)