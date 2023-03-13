
import threading
import random
import time

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def is_full(self):
        return (self.tail + 1) % self.size == self.head

    def is_empty(self):
        return self.head == -1

    def enqueue(self, data):
        while True:
            self.lock()
            if not self.is_full():
                if self.head == -1:
                    self.head = 0
                self.tail = (self.tail + 1) % self.size
                self.queue[self.tail] = data
                self.unlock()
                return
            self.unlock()
            time.sleep(1)

    def dequeue(self):
        while True:
            self.lock()
            if not self.is_empty():
                data = self.queue[self.head]
                if self.head == self.tail:
                    self.head = self.tail = -1
                else:
                    self.head = (self.head + 1) % self.size
                self.unlock()
                return data
            self.unlock()
            time.sleep(1)

def producer():
    while True:
        num = random.randint(1, 10)
        time.sleep(num)
        q.enqueue(num)
       



def consumer():
    while True:
       
        rand_num = random.randint(1, 10)
        time.sleep(rand_num)
        data_dequeued = q.dequeue()
        print(f"Dequeued item: {data_dequeued}")
     



if __name__ == '__main__':

    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


