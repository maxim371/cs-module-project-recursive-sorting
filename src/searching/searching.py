# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if end >= start:
        mid = start + (end - start) // 2

        # if mid found, return mid
        if arr[mid] == target:
            return mid

        # search left half
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
            # search left half
        else: #arr[mid] < target
            return binary_search(arr, target, mid + 1, end)

    else:
        return -1


        


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) - 1
    if arr[start] == arr[end]:
        if target == arr[start]:
            return start
        else:
            return - 1
    # boolean to keep track of array descending or ascending
    is_ascending = arr[start] < arr[end]
    # array ascending?, perform normal binary search
    if is_ascending:
        return binary_search(arr, target, 0, len(arr) - 1)
    # array descending?, perfrom reverse binary search
    else:
        return descending_binary_search(arr, target, 0, len(arr) - 1)

def descending_binary_search(arr, target, start, end):
    if start > end:
        return - 1
    else:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return descending_binary_search(arr, target, mid + 1, end)
        else:
            return descending_binary_search(arr, target, start, mid - 1)

array = [-1, 0, 1, 9, 10, 28]
target = 9
result = binary_search(array, target, 0, len(array) - 1)
print(f'target index: {result}')


