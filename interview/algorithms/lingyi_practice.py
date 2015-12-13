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
import numpy.random as nprnd


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


merge_sort_test()
