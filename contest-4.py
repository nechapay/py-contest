# Given a python list of integers, you need to print True if 4 contains another 4 next to it
# in the list. If such a thing doesn't occur then print False.
def has44(arr):
    for i in range(len(arr)-1):
        if arr[i] == 4 and arr[i+1] == 4:
            return True
    return False

# You are given a list of integers. You need to return the average of the list, except ignore the maximum
# and the minimum value. If there are multiple copies of the smallest value, ignore just one copy,
# and likewise for the largest value. Use int division (or floor to int) to produce the final average.
# You may assume that the array is length 3 or more.


def avg(mylist):
    mx = max(mylist)
    mn = min(mylist)
    sum = 0
    count = 0
    for i in range(len(mylist)):
        sum += mylist[i]
        count += 1
    sum = sum - mn - mx
    count -= 2
    return int(sum/count)


# You are given a list. Print the sum of the list numbers. If the list is empty, then 0 gets printed.
# Also, the element 7 and the element next to it won't contribute to the sum.

def realSum(mylist):
    i = 0
    sum = 0
    while i < len(mylist):
        if mylist[i] == 7:
            i += 2
            continue
        sum += mylist[i]
        i += 1
    return sum
