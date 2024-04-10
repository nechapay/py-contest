# Given a statement containing some words (lowercase characters) which may have some repeating words.
# The task is to count the frequency of each word in the statement.

def frequency_word(statement):
    l = statement.split()
    d = {}

    for i in l:
        d[i] = 0
    for i in l:
        d[i] += 1
    li = []
    for i in l:
        if i in li:
            continue
        li.append(i)

    for k in li:
        print(k, d[k] if d[k] > 1 else '')


frequency_word(
    'this is the man who did this task which is the task to be done by another man')

# Given a list of positive integers (numbers may be repeated). The task is to print the numbers in sorted order.
# Numbers occurring more than once should be printed once.


def sorted_elements(arr):
    s = set(arr)
    li = list(s)
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if int(li[i]) > int(li[j]):
                t = int(li[i])
                li[i] = int(li[j])
                li[j] = t
    return li


# print(sorted_elements([7, 6, 7, 3, 28, 7]))

# Given a list of positive integers and a number K. In the list, every element occurs K times except one.
# The task is to find the element not present K times. If no such element exists then print -1.


def find_lonely(numbers, K):
    d = {}
    for i in numbers:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for x in d:
        if not (d[x] == K):
            return x

    return -1


# print(find_lonely([1, 8, 7, 2, 1, 7, 1, 8, 7, 8], 3))
