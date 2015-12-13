import numpy as np
import numpy.random as nprnd

# Coding interview - 9.4
# Finding all subsets in a set
# Iterative solution using bit shifting

output = []


def find_subset(data):
    data_len = len(data)
    for i in range(0, pow(2, data_len)):
        cur_output = []
        for j in range(0, data_len):
            flag = bool(i & (1 << j))
            if flag:
                cur_output.append(data[j])
        output.append(cur_output)


def find_subset_test():
    global output
    for i in range(0, 4):
        data = [x for x in range(0, i)]
        print "Data: ", data
        output = []
        find_subset(data)
        print "Output: ", output, "\n"


# Coding interview - 11.1
# Merge sort
def merge_sort(data):
    if len(data) == 1:
        return data

    mid = len(data) // 2
    lhs = data[:mid]
    rhs = data[mid:]
    lptr = 0
    rptr = 0
    ret = []

    lhs = merge_sort(lhs)
    rhs = merge_sort(rhs)

    while lptr < len(lhs) and rptr < len(rhs):
        if lhs[lptr] < rhs[rptr]:
            ret.append(lhs[lptr])
            lptr += 1
        else:
            ret.append(rhs[rptr])
            rptr += 1

    if lptr < len(lhs):
        ret.extend(lhs[lptr:])
    else:
        ret.extend(rhs[rptr:])

    return ret


def merge_sort_test():
    data = nprnd.randint(1000, size=10)
    print "Input: ", data
    print "Output:", merge_sort(data)


# 11.3
# sorted array of n integers that has been rotated
# write code to find an element in the array

def rotated_sort(data, value):
    # Use binary search the find the actual start point
    low = 0
    high = len(data) - 1
    mid = 0

    # Search the switch point
    if data[high] < data[low]:
        while high - low >= 0:
            mid = (low + high) // 2
            if data[mid] > data[mid + 1]:
                break
            elif data[mid] > data[0]:
                low = mid + 1
            else:
                high = mid - 1

    switch_point = mid
    low = 0
    high = len(data) - 1

    #  Normal binary search
    while high - low >= 0:
        mid = ((low + high) // 2 + switch_point) % len(data)
        if data[mid] == value:
            return mid
        elif data[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def rotated_sort_test():
    data1 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    data2 = [x for x in range(0, 10)]
    data = [data1, data2]
    for data in data:
        print "Input: ", data
        print "Output: ", rotated_sort(data, 5)


# rotated_sort_test()

# 9.8
# Making change

# Minimum number of coins needed
def make_change1(amount, denom):
    min_coins = np.zeros(amount + 1)
    coin_used = np.zeros(amount + 1)
    for i in range(amount + 1):
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
    for i in range(0, amount + 1, denom_amount):
        ways += make_change(amount - i, denom, index + 1, c_map)
    c_map[amount][index] = ways
    return ways


def make_change_test():
    denom = [100, 50, 25, 10, 5, 1]
    n = 100
    c_map = np.zeros((n + 1, len(denom)))
    result = make_change(n, denom, 0, c_map)
    print result


# 9.9
# N-queens

def check_diag(i, placed, col, pos):
    if placed == 0:
        return True
    check_row = placed
    check_col = i
    for j in range(0, placed):
        cur_row = j
        cur_col = pos[j]
        diff_col = abs(cur_row - check_row)
        diff_row = abs(cur_col - check_col)
        if diff_col == diff_row:
            return False
    return True


def n_queens(n, placed, col, pos):
    if placed == n:
        return 1
    ways = 0
    for i in range(n):
        if not col[i] and check_diag(i, placed, col, pos):
            col[i] = True
            pos[placed] = i
            ways += n_queens(n, placed + 1, col, pos)
            col[i] = False
    return ways


def n_queens_test():
    n = 11
    col = [False] * n
    pos = [-1] * n
    print n_queens(n, 0, col, pos)


n_queens_test()
