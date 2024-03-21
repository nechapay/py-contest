# You are given a mean M, and an integer D. The mean M is the mean of 3 numbers A, B, and C.
# Find the mean of A, B, C, and D. Note : Mean is the average of the given numbers and is calculated
# by dividing the sum of given numbers by the total number of numbers.
import math


def mean(D, M):
    # Your code here
    return int(((M * 3) + D) / 4)


# You are given two numbers A and B. When A is raised to some power P, we get a number X.
# Now, you need to find what is the value of X that is closest to B.


def nearestPower(A, B):
    # Your code here
    # return the A ** math.log(A, B) closest power
    p = int(math.log(B)/math.log(A))
    low = A ** p
    high = A * low

    if (B - low) < (high - B):
        return low
    return high

# You are given a two-digit number N. Find the sum of its digits


def digitsSum(N):
    # Your code here
    sum = 0
    for x in str(N):
        sum += int(x)
    return sum
