"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""


def has_duplicates(product_ids):
# I chose a set because it stores unique values and provides efficient membership checking.
# As I loop through the product IDs, checking and adding values to the set are O(1) on average.
# Each product ID is checked at most once, so the overall time complexity is O(n).
    
    seen_ids = set()

    for product_id in product_ids:
        if product_id in seen_ids:
            return True
        seen_ids.add(product_id)

    return False


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
    # I chose a queue because tasks need to stay in the order they were added, following First In, First Out (FIFO).
    # Adding a task to the end of the list with append() is O(1) on average.
    # Removing the oldest task with pop(0) is O(n) because the remaining tasks have to shift.
        
         self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if self.tasks:
            return self.tasks.pop(0)
        return None



"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
   # I chose a set because it stores unique values and does not allow duplicates.
   # Adding a value to the set is O(1) on average, and getting the count with len() is O(1).
   # This makes it easy to keep track of the number of unique values as new values are added.

        self.values = set()

    def add(self, value):
        self.values.add(value)


    def get_unique_count(self):
        return len(self.values)
    


# Test the practice problems using the examples from the assignment


print(has_duplicates([10, 20, 30, 20, 40]))
print(has_duplicates([1, 2, 3, 4, 5]))

task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
print(task_queue.remove_oldest_task())

tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
print(tracker.get_unique_count())
