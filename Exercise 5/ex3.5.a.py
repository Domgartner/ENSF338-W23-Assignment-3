import random
import time
import matplotlib.pyplot as plt

# Inefficient implementation
# implementation of linear search takes O(n) time in the worst case, where n is the size of the input array.
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Efficient implementation
# implementation of binary search takes O(log n) time in the worst case, where n is the size of the input array.
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Function to time the search function
def time_search(search_fn, arr, x, num_trials):
    times = []
    for i in range(num_trials):
        start_time = time.time()
        search_fn(arr, x)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

# Function to plot the distribution of measured values
def plot_times(task_name, inefficient_time, efficient_time):
    fig, ax = plt.subplots()
    ax.hist([inefficient_time, efficient_time], color=['r', 'b'], alpha=0.5, label=['Inefficient', 'Efficient'])
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Frequency')
    ax.set_title(task_name)
    ax.legend()
    plt.show()

# Function to run the experiment
def run_experiment(task_name, arr_size, num_trials):
    arr = sorted([random.randint(0, arr_size) for i in range(arr_size)])
    x = random.randint(0, arr_size)
    linear_times = time_search(linear_search, arr, x, num_trials)
    binary_times = time_search(binary_search, arr, x, num_trials)
    print(task_name)
    print(f'Linear search: min={min(linear_times):.6f}s, avg={sum(linear_times)/num_trials:.6f}s')
    print(f'Binary search: min={min(binary_times):.6f}s, avg={sum(binary_times)/num_trials:.6f}s')
    plot_times(task_name, linear_times, binary_times)

# Run the experiment
if __name__ == '__main__':
    run_experiment('Search in a sorted array', 1000, 100)
