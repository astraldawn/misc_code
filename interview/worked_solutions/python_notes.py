# Functionality in external library
#   2D array declaration - using numpy
#   Code?
# xrange vs range
#   xrange: generator like object
#   range: list
# ( ) generator, [ ] list comprehension
# The difference between == and is
#    ==: if the objects referred by the variables are equal
#   is: variables point to the same object
# Shallow vs. deep copying
#   Shallow copy: the top layer of the object
#   Deep copy: the entire object
#   For primitives: shallow copy is equivalent to deep copy
#   e.g. result = [[0] * col] * row
#   [0] * col works fine because it is constructing shallow copies
#   * row does not as what it does is it creates 3 references to the same object
# Binary search
#   The proper way
#   Bisect function (show them this first)
# DP: memorise coin change / knapsack
# Other python stuff
#   os.walk
#   hashlib (md5)
# Dictionary keys and values (how the default iteration looks like)


# 2D array
import numpy as np

row = 5
col = 5
dv = 0

a = np.empty((row, col))
a.fill(dv)

b = [[dv] * col for j in xrange(row)]

# xrange vs. range
# always use xrange, range generates the list full list
a = xrange(5)
b = range(5)


# Generator vs. list comprehension
# Generator just comes up with a convenient object that can be iterated
def first_n(n):
    num = 1
    while num <= n:
        yield num
        num += 1


a = sum(first_n(100))
b = sum(xrange(1, 101))
c = sum([x for x in range(1, 101)])


# The difference between == and is
#    ==: if the objects referred by the variables are equal
#   is: variables point to the same object
#
# Immutable types: int float long complex str / bytes tuple / frozen set
# Mutable types: byte array / list / set / dict

# Binary search
#   The proper way
#   Bisect function (show them this first)

# The proper way
def binary_search_find(A, value):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = low + (high - low) / 2
        if A[mid] == value:
            return mid
        elif A[mid] >= value:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def binary_search_left(A, value):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = low + (high - low) / 2
        if A[mid] >= value:  # Leftmost insertion point (rightmost is >)
            high = mid - 1
        else:
            low = mid + 1

    return low


import bisect


def binary_search_find_python(A, value):
    high = len(A) - 1
    pos = bisect.bisect_left(A, value)

    if pos <= high:
        return pos

    return -1


A = range(5)
B = [binary_search_find(A, x) for x in range(6)]
B1 = [binary_search_find_python(A, x) for x in range(6)]
C = [binary_search_left(A, x) for x in range(6)]
D = [bisect.bisect_left(A, x) for x in range(6)]
E = [bisect.bisect_right(A, x) for x in range(6)]
print A, B, B1, C, D, E


# Coin change DP
# 9.8
# Making change

# Minimum number of coins needed
def make_change1(amount, denom):
    min_coins = np.zeros(amount + 1)
    coin_used = np.zeros(amount + 1)
    for i in xrange(amount + 1):
        coin_count = i
        new_coin = 1
        for j in [k for k in denom if k <= i]:
            if min_coins[i - j] + 1 < i:
                coin_count = min_coins[i - j] + 1
                new_coin = j
        min_coins[i] = coin_count
        coin_used[i] = new_coin
    return min_coins[amount]


# Number of ways to make change
def make_change(amount, denom, index, c_map):
    if c_map[amount][index] > 0:
        return c_map[amount][index]
    if index >= len(denom) - 1:
        return 1
    denom_amount = denom[index]
    ways = 0

    # Make a smaller amount without the current coin
    for i in xrange(0, amount + 1, denom_amount):
        ways += make_change(amount - i, denom, index + 1, c_map)
    c_map[amount][index] = ways
    return ways


def make_change_better(n, denom, ways):
    for coin in denom:
        for i in xrange(coin, n + 1):
            ways[i] += ways[i - coin]
    return ways[n]


def make_change_test():
    denom = [25, 10, 5, 1]
    n = 25
    c_map = np.zeros((n + 1, len(denom)))
    # result = make_change(n, denom, 0, c_map)
    ways = [1] + [0] * n
    result = make_change_better(n, denom, ways)
    print result


# Knapsack

# os.walk

# Hashing
import hashlib

# Using a block is important when dealing with files that may be very large
BLOCKSIZE = 65536
hasher = hashlib.md5()
with open('anotherfile.txt', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print(hasher.hexdigest())

# Dictionary keys and values
A = {'a': 1, 'b': 2, 'c': 3}
print A.keys()
print A.values()
print [x for x in A]  # Default iterator through dictionary is keys
print [x for x in A.iteritems()]  # Iterates through the entire dictionary

# Collections
from collections import defaultdict

A = defaultdict(list)  # int can be used also
A['a'].append('x')
A['a'].append('5')
print A

# Random number generator
from random import randint

print randint(0, 63)  # Returns random integer N such that 0 <= N <= 63
