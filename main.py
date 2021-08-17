# implementation of binary search algorithm

# I will prove that binary search is faster than naive search

# Naive search basically search every index iteratively and ask if it is equal to target value
# if array consists the value it returns
# if it is not in the array it returns -1
import random
import time

def naive_search(l, target):
    # example l = [1,2,3,4,18]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search uses divide and conquer method
# we will leverage the fact that our list is sorted.

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1
    midpoint = (low + high) // 2
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint + 1, high)


if __name__ == '__main__':
    # l = [1, 15, 25, 60, 79, 90]
    # target = 90
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 1000

    # build a sorted list of length 1000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    start= time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time :", (end-start)/length, " seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list,target)
    end = time.time()
    print("Binary search time :", (end-start)/length, " seconds")
