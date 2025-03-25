"""
621. Task Scheduler
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)  # Count occurrences of each task
        max_heap = [-count for count in task_counts.values() if count > 0]  # Max heap for task frequencies
        heapq.heapify(max_heap)
        
        time = 0
        cool_down = deque()  # Track tasks in cooldown (FIFO queue)
        
        while max_heap or cool_down:
            time += 1  # Every iteration represents a CPU interval
            
            if max_heap:
                freq = -heapq.heappop(max_heap)  # Get most frequent task
                if freq > 1:
                    cool_down.append((freq - 1, time + n))  # Store (remaining count, ready time)
            
            # Check if a task in cooldown is ready to be scheduled again
            if cool_down and cool_down[0][1] == time:
                heapq.heappush(max_heap, -cool_down.popleft()[0])  # Push back into heap
        
        return time