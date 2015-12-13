# Coding interview - 9.4
# Finding all subsets in a set
# Iterative solution using bit manipulation

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


for i in range(0, 4):
    data = [x for x in range(0, i)]
    print data
    output = []
    find_subset(data)
    print output
