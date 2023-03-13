
import sys

lst = []
prev_capacity = sys.getsizeof(lst)

for i in range(64):
    lst.append(i)

    curr_capacity = sys.getsizeof(lst)

    if curr_capacity != prev_capacity:

        print(f"Capacity has changed from {prev_capacity} bytes to {curr_capacity} bytes at {i+1} elements")
        
        prev_capacity = curr_capacity
