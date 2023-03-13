import json
import timeit
import matplotlib.pyplot as plt

def task_search(task):
    best_mid = len(data_data) // 2
    best_time = float('inf')
    f = [0, len(data_data)//4, len(data_data)//2, 3*len(data_data)//4, len(data_data)-1]
    for i in f:
        elapsed_time = timeit.timeit(lambda: binary_search(data_data, task, mid=i), number=1)
        if elapsed_time < best_time:
            best_time = elapsed_time
            best_mid = i

    return best_mid

def binary_search(arr, x, start=0, end=None, mid=None):
    if end is None:
        end = len(arr)
    if mid is None:
        mid = (start + end) // 2
    if end <= start:
        return False
    if arr[mid] == x:
        return True
    elif arr[mid] > x:
        return binary_search(arr, x, start, mid, (start + mid) // 2)
    else:
        return binary_search(arr, x, mid + 1, end, (mid + end) // 2)

if __name__ == '__main__':

    data = open('Exercise2/ex2data.json', 'r')
    data_data = json.load(data)
    data.close()
    task = open('Exercise2/ex2tasks.json', 'r')
    tasks_data = json.load(task)
    task.close()

    x_vals = []
    y_vals = []

    for i in tasks_data:
        best_midpoint = task_search(i)
        print(f"best midpoint for {i} is: {best_midpoint}")
        x_vals.append(i)
        y_vals.append(best_midpoint)

    plt.scatter(x_vals, y_vals)
    plt.xlabel('Search Task')
    plt.ylabel('Chosen Midpoint')
    plt.show()


# import json
# import timeit
# import matplotlib.pyplot as plt

# def task_search(task):
#     best_mid = len(data_data) // 2
#     best_time = float('inf')
#     f = [0, len(data_data)//4, len(data_data)//2, 3*len(data_data)//4, len(data_data)-1]
#     for i in f:
#         elapsed_time = timeit.timeit(lambda: binary_search(data_data, task, mid=i), number=1)
#         if elapsed_time < best_time:
#             best_time = elapsed_time
#             best_mid = i

#     return best_mid

# def binary_search(arr, x, start=0, end=None, mid=None):
#     if end is None:
#         end = len(arr)
#     if mid is None:
#         mid = (start + end) // 2
#     if end <= start:
#         return False
#     if arr[mid] == x:
#         return True
#     elif arr[mid] > x:
#         return binary_search(arr, x, start, mid, (start + mid) // 2)
#     else:
#         return binary_search(arr, x, mid + 1, end, (mid + end) // 2)

# if __name__ == '__main__':

#     data = open('Exercise2/ex2data.json', 'r')
#     data_data = json.load(data)
#     data.close()
#     task = open('Exercise2/ex2tasks.json', 'r')
#     tasks_data = json.load(task)
#     task.close()

#     x_vals = []
#     y_vals = []

#     for i in tasks_data:
#         best_midpoint = task_search(i)
#         print(f"best midpoint for {i} is: {best_midpoint}")
#         x_vals.append(i)
#         y_vals.append(best_midpoint)

#     plt.scatter(x_vals, y_vals, c=y_vals, cmap='Greys')
#     plt.xlabel('Search Task')
#     plt.ylabel('Chosen Midpoint')
#     plt.colorbar()
#     plt.show()


