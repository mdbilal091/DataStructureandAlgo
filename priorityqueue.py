""" Creating the Priority Queue Class """

import heapq

class priorityqueue:

    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def get(self):
        return heapq.heappop(self.elements)[1]

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority,item))

    def __str__(self):
        return str(self.elements)

def process_task(tasks):
    pq1 = priorityqueue()

    for task,priority in tasks:
        pq1.put(task,priority)
    #print(pq1)

    ordered_task_list = []
    while not pq1.is_empty():

        ordered_task_list.append(pq1.get())

    return ordered_task_list


if __name__ == "__main__":

    pq = priorityqueue()

    #print(pq)

    #print(pq.is_empty())

    pq.put(" Hundreth Code", 100)
    pq.put("First Code", 1)
    pq.put("Zero Code", 0)
    pq.put("Second Code", 1)
    pq.put("fourth Code", 4)
    pq.put(" tenth Code", 10)

    #print(pq)

    #print(pq.get())
    #print(pq.get())
    #print(pq.get())
    #print(pq.get())
    #print(pq.get())
    #print(pq.get())

    tasks = [("drink",2),("eat",1),("be merry", 3)]

    result_q = process_task(tasks)
    print(result_q)

