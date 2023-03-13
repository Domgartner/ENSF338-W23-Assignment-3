import random
import heapq
import matplotlib.pyplot as plt
import timeit

class PriorityQueueInefficient:
    def __init__(self):
        self.elements = []

    def put(self, item, priority):
        self.elements.append((priority, item))

    def get(self):
        try:
            _, item = min(self.elements)
        except ValueError:
            return None
        self.elements.remove((_, item))
        return item

class PriorityQueueEfficient:
    def __init__(self):
        self.elements = []

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        try:
            _, item = heapq.heappop(self.elements)
        except IndexError:
            return None
        return item


def experiment():
    # Generating random inputs
    inputs = random.sample(range(1000000), 1000)

    # Inefficient priority queue
    t1 = timeit.Timer(lambda: inefficient_priority_queue(inputs))
    inefficient_time = t1.timeit(number=100)
    print("Inefficient priority queue took:", inefficient_time)

    # Efficient priority queue
    t2 = timeit.Timer(lambda: efficient_priority_queue(inputs))
    efficient_time = t2.timeit(number=100)
    print("Efficient priority queue took:", efficient_time)

    # Plotting the distribution of measured values
    fig, ax = plt.subplots()
    ax.hist(inefficient_time, color='r', alpha=0.5, label='Inefficient')
    ax.hist(efficient_time, color='b', alpha=0.5, label='Efficient')
    ax.set_xlabel('Execution Time (s)')
    ax.set_ylabel('Frequency')
    ax.set_title('Priority Queue Execution Time')
    ax.legend()
    ax.set_xlim([0, ax.get_xlim()[1]])
    plt.show()

    # Printing the aggregate of the measured values
    print("Time for inefficient priority queue (s):", inefficient_time)
    print("Time for efficient priority queue (s):", efficient_time)


def inefficient_priority_queue(inputs):
    pq = PriorityQueueInefficient()
    for i in inputs:
        pq.put(i, i)
    pq_list = []
    for i in range(len(inputs)):
        pq_list.append(pq.get())
    return pq_list


def efficient_priority_queue(inputs):
    pq = PriorityQueueEfficient()
    for i in inputs:
        pq.put(i, i)
    efficient_list = []
    for i in range(len(inputs)):
        efficient_list.append(pq.get())
    return efficient_list


if __name__ == '__main__':
    experiment()
