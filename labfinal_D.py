import math

def manhattan(arr):
    return sum([abs(num) for num in arr])

def euclidean(arr):
    return math.sqrt(sum([math.pow(num, 2) for num in arr]))

def chebyshev(arr):
    return max([abs(num) for num in arr])

N = int(input())
arr = [int(x) for x in input().split(" ")]
print(manhattan(arr))
print(euclidean(arr))
print(chebyshev(arr))
