from bisect import bisect_right as br, bisect_left as bl

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    for i in range(elements):
        if not arrA:
            merged_arr[i] = arrB.pop(0)
        elif not arrB:
            merged_arr[i] = arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
        elif arrB[0] < arrA[0]:
            merged_arr[i] = arrB.pop(0)
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    len_arr = len(arr)
    if len_arr > 1:
        split = len_arr // 2
        left = merge_sort(arr[:split])
        right = merge_sort(arr[split:])
        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):  
    new = mid + 1

    if arr[mid] <= arr[new]:
        return

    while start <= mid and new <= end:

        if arr[start] <= arr[new]:
            start += 1
        else:
            value = arr[new]
            index = new

            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            start += 1
            mid += 1
            new += 1

def merge_sort_in_place(arr, l, r):
    if (r - l) > 1:

        mid = 1 + (r - l) // 2
        # sort first and second halfs
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid, r)
        
        merge_in_place(arr, l, mid, r)    


# def printList(array):
#     for ii in range(len(array)):
#         print(array[ii], end=', ')

# arrA = [0, 33, 44, 77]
# arrB = [-1, 22, 77, 99]

# _merge_ = merge(arrA, arrB)

# array = [4, 2, 1, 0, 7, 5, 12, -4]
# array_2 = [44, 33, 22, 0, 77, 55, 44, -11]

# sorted_1 = merge_sort(array)
# print('\n')


