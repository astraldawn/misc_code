import sys

'''
N floors, K eggs

With 1 egg: N drops WC
With infinite egg: log2(N) drops WC (binary search)

Assume N = 100
Worst case: 7

3
1: 1 100 50
2: 1 49 25
3: 1 24 12
4: 1 11 6
5: 1 5 3
6: 4 5 4
4 3 4 --> At the end, we know that egg survives at 3, breaks at 4
6

The more specific case (N = 100, K = 2)
Binary search won't work. Many drops are needed if it breaks on the first
drop. (50).

We can go up the floors in 10s. So if it breaks on the first drop (10),
then we need only try 9 further drops.

If it breaks on floor 99, then we would have made 10 drops (from 10 .. 100)
and then need to make 9 drops from 91 to 99. [WC = 19]

We realise now that if the egg breaks on a lower floor, we need to use less
drops than if it breaks on a higher floor.

Consider the case where we drop the egg on floor n.
If we breaks, then we have to try n-1 floors.

However, if it doesn't break, our previous approach involved going up by n
floors (10) and trying again, for another step with n drops.

However, we have already used 1 drop, so we should only go up by n-1 floors.
So the next floor to try is n + (n-1).

Extending this argument, the next floor to try (if the egg doesn't break) is
n + (n-1) + (n-2) ...

This eventually leads to the equation: n + (n-1) + (n-2) + .... + 2 + 1 = (
n)(n+1)/2

So now we need to solve this equation for 100 floors. Which gives a result of 13.651
(pretend to calculate here)
'''

N_eggs = 1
N_floors = 1000

max_drop = [[-1 for y in range(0, N_eggs + 1)] for x in range(0, N_floors + 1)]

# Base case with 0 floors / 1 floor + any amount of eggs
for i in range(1, N_eggs + 1):
    max_drop[1][i] = 1
    max_drop[0][i] = 0

# Base case for n floors with 1 egg
for i in range(1, N_floors + 1):
    max_drop[i][1] = i

# n floors, k eggs
def calc_drop(n, k):
    if max_drop[n][k] != -1:
        return max_drop[n][k]

    min_res = sys.maxint
    for i in range(1, n + 1):
        # The egg breaks, reduce problem to tower of height i - 1 with e - 1
        # eggs
        r1 = calc_drop(i - 1, k - 1)

        # The egg does not break, need to check floors - i eggs, still have eggs
        r2 = calc_drop(n - i, k)

        res = max(r1, r2)
        min_res = min(res, min_res)
    max_drop[n][k] = min_res + 1
    return max_drop[n][k]

# n floors and k eggs
def eggDrop_iterative_dp(k, n):
    # A 2D table where entery eggFloor[i][j] will represent minimum
    # number of trials needed for i eggs and j floors.
    eggFloor = [[0 for x in range(n + 1)] for x in range(k + 1)]

    # We need one trial for one floor and0 trials for 0 floors
    for i in range(1, k + 1):
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0

    # We always need j trials for one egg and j floors.
    for j in range(1, n + 1):
        eggFloor[1][j] = j

    # Fill rest of the entries in table using optimal substructure
    # property
    for i in range(2, k + 1):
        for j in range(2, n + 1):
            eggFloor[i][j] = sys.maxint
            for x in range(1, j + 1):
                res = 1 + max(eggFloor[i - 1][x - 1], eggFloor[i][j - x])
                if res < eggFloor[i][j]:
                    eggFloor[i][j] = res

    # eggFloor[n][k] holds the result
    return eggFloor[k][n]


# print calc_drop(N_floors, N_eggs)
# print eggDrop_iterative_dp(N_eggs, N_floors)

def eggDrop_lower(floors, break_floor, trace=False):
    low = 0
    high = floors - 1
    mid = 0
    iteration = 0
    while low <= high:
        mid = (low + high) // 2
        iteration += 1
        if trace:
            print low + 1, high + 1, mid + 1
        # the egg survives
        if mid <= break_floor:
            low = mid + 1
        else:
            high = mid - 1
    if trace:
        print low + 1, high + 1, mid + 1
    return iteration


def eggDrop_lowertest():
    N = 1000
    worst_case = 10
    cnt = 0
    for i in range(0, N):
        res = eggDrop_lower(N, i)
        if res < worst_case:
            cnt += 1
            print i + 1
            print eggDrop_lower(N, i, trace=True)
    print "NUMBER OF BETTER CASES: ", cnt


eggDrop_lowertest()
