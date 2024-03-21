# Given a non-negative number N, print True if N is within 2 of a multiple of 10, else print false.
# For example, 22 is within 2 of a multiple of 10 (the multiple here is 20) and 23 is not within 2 of a
# multiple of 10 (it is within 3 of multiple 20).

def isNeighbour(N):
    return not (2 < (N % 10) < 8)


# Given 2 integers, A and B, print their sum. However, if the sum is in the range (20-40) both inclusive,
# then just return 42 only.

def aweSum(A, B):
    s = A + B
    return s if not (20 <= s <= 40) else 42


# You are given a string str of lowercase letters. You need to count the number of times the word
# doge appears in the string. Also, the g in doge can be replaced by any letter from a - z so dope is also valid.

def doge_count(str):
    count = 0
    if len(str) < 4:
        return count
    for x in range(len(str) - 3):
        if (str[x:x+2] == 'do' and str[x+3] == 'e'):
            count += 1
    # Your code here
    return count
