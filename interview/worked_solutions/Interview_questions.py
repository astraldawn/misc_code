# List of interview questions that I decide to attempt
from collections import defaultdict


# Evaluate expressions: a = "+(+(1,2), +(2,3))"
# Notable assumptions include: the expression is valid, notably there will be
#  no things such as divide by 0 errors. In this solution every operation on
# the stacks is guaranteed to be O(1)
def daniel_google_q2(expr):
    operators = ['+', '-', '*', '/']
    operator_stack = []
    number_stack = []
    curr_num = None
    for c in expr:
        if c in operators:
            operator_stack.append(c)
        elif c.isdigit():
            if curr_num is None:
                curr_num = int(c)
            else:
                curr_num = curr_num * 10 + int(c)
        elif c == ',':
            if curr_num:
                number_stack.append(curr_num)
                curr_num = None
        elif c == ')':
            if curr_num:
                number_stack.append(curr_num)
                curr_num = None
            curr_opr = operator_stack.pop()
            n2 = number_stack.pop()
            n1 = number_stack.pop()
            if curr_opr == '+':
                number_stack.append(n1 + n2)
            elif curr_opr == '*':
                number_stack.append(n1 * n2)
            elif curr_opr == '-':
                number_stack.append(n1 - n2)
            elif curr_opr == "/":
                number_stack.append(n1 / n2)

    return number_stack[0]


daniel_google_q2_test1 = "+(+(15,12), *(2,3))"


# print daniel_google_q2(daniel_google_q2_test1)

# Cumulative sum on a 2D array
def royson_google_q1(inp):
    row = len(inp) + 1
    col = len(inp[0]) + 1
    result = [[0 for _ in range(col)] for _ in range(row)]
    print result
    for i in xrange(1, row):
        for j in xrange(1, col):
            result[i][j] = (inp[i - 1][j - 1] + result[i - 1][j] +
                            result[i][j - 1] - result[i - 1][j - 1])

    return [x[1:] for x in result[1:]]


royson_google_q1_test1 = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]
res = royson_google_q1(royson_google_q1_test1)
for _ in res:
    print _


# Given voting record (timestamp, candidate voted) write a function
# getTop(input, T) which returns top candidate on time T.
#
# input = [(timestamp, candidate voted)]
# 10 A
# 20 B
# 30 A
# 40 C
# 50 B
# 60 D
# 70 C
# 80 C
# getTop(input, 43) -> A
# getTop(input, 86) -> C
def royson_google_q2(inp, time):
    max_count = 0
    votes = defaultdict(int)
    votes_max = defaultdict(list)
    for (t, v) in inp:
        if t > time:
            return votes_max[max_count][0]
        votes[v] += 1
        max_count = max(votes[v], max_count)
        votes_max[votes[v]].append(v)

    return votes_max[max_count][0]


royson_google_q2_test1 = [(10, 'A'), (20, 'B'), (30, 'A'), (40, 'C'), (50, 'B'),
                          (60, 'D'), (65, 'E'), (70, 'C'), (80, 'C')]

# print royson_google_q2(royson_google_q2_test1, 43)
# print royson_google_q2(royson_google_q2_test1, 86)
