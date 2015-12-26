# Chapter 1 - Arrays and Strings
# Additional questions
#   - Bit manipulation 5.7
#   - Object orientated design 8.10
#   - Recursion 9.3
#   - Sorting and searching 11.6
#   - C++ 13.10
#   - Moderate 17.7 17.8 17.14

# 1.1 Implement algorithm to determine if a string has all unique chars. Do not
# use any additional data structures
#    - (Ask) Assume the string is ASCII


def one_one(s):
    checker = 0
    for c in s:
        offset = ord(c)
        if (checker & (1 << offset)) > 0:  # Check if the bit is set
            return False
        checker |= 1 << offset  # Set the bit
    return True


def test_one_one():
    print one_one("Hello world")
    print one_one("Bye world")


# 1.2 Implement a function to reverse a string
def one_two(s):
    return ''.join(reversed(s))  # More readable
    # return s[::-1] # The fastest solution


def test_one_two():
    print one_two("hello world")


# 1.3 Given two strings, write a method to decide if one is permutation of
# the other
#   - Assume the strings are ASCII
def one_three(s1, s2):
    if len(s1) != len(s2):
        return False
    store = [0] * 256
    for c in s1:
        store[ord(c)] += 1
    for c in s2:
        store[ord(c)] -= 1
        if store[ord(c)] < 0:
            return False
    return True


def test_one_three():
    print one_three("asdf", "asdfg")
    print one_three("Hello world", "world Hello")
    print one_three("Hello Hello", "World Hello")


# 1.4 Write a method to replace all spaces in a string with '%20'. You may
# assume that the string has sufficient space at the end of the string to
# hold the additional characters and that you are given the "true" length of
# the string.
def one_four(s, len):
    return s[:len].replace(' ', '%20')


def test_one_four():
    print one_four("Mr John Smith    ", 13)


# 1.5 Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become
# a2b1c5a3. If the compressed string would not become smaller than the
# original string, return the original string
def one_five(s):
    # Using a list to build the results and then joining together at the end
    # is similar to the java stringbuilder
    output = []
    cur_char = s[0]
    count = 0
    for c in s:
        if cur_char is not c:
            output.append(cur_char + str(count))
            cur_char = c
            count = 1
        else:
            count += 1

    output.append(cur_char + str(count))
    output = ''.join(output)

    return output if len(output) < len(s) else s


def test_one_five():
    print one_five("aabcccccaaa")
    print one_five("abcd")


# 1.6 Given an image represented by an N x N matrix, where each pixel in the
# image is 4 bytes, write a method to rotate the image by 90 degrees. Can you
#  do this in place?
#
# Perform a swap by index, working inward layer by layer
def one_six(matrix):
    n = len(matrix)
    for layer in range(0, n / 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]  # Save top
            matrix[first][i] = matrix[last - offset][first]  # top = left
            # left = bottom
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]  # bottom = right
            matrix[i][last] = top  # right = top
    return matrix


def test_one_six():
    res = one_six([[1, 1, 1, 1],
                   [2, 2, 2, 2],
                   [3, 3, 3, 3],
                   [4, 4, 4, 4]
                   ])

    for row in res:
        print row


# 1.7 Write an algorithm such that if an element in an M x N matrix is 0,
# its entire row and column are set to 0
# This solution uses O(1) memory, as the first row and first col are used to
# hold values for the rest of the rows / cols
def one_seven(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Check if any items in the first row are 0
    first_row_zero = False
    for i in range(0, cols):
        if matrix[0][i] == 0:
            first_row_zero = True

    # Check if any items in the first col are 0
    first_col_zero = False
    for i in range(0, rows):
        if matrix[i][0] == 0:
            first_col_zero = True

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(0, rows):
        if matrix[i][0] == 0:
            for j in range(0, cols):
                matrix[i][j] = 0

    for i in range(0, cols):
        if matrix[0][i] == 0:
            for j in range(0, rows):
                matrix[j][i] = 0

    # Set the first row to 0
    if first_row_zero:
        matrix[0] = [0] * cols

    # Set the first col to 0
    if first_col_zero:
        for i in range(0, rows):
            matrix[i][0] = 0

    return matrix


def test_one_seven():
    res = one_seven([[1, 1, 0, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1]
                     ])

    for row in res:
        print row

# 1,8 Assume you have a method isSubString which checks if one word is a
# substring of another. Given two strings, s1 and s2, write code to check if
# s2 is a rotation of s1 using only one call to isSubString

# def one_eight(s1, s2):
#     if len(s1) != len(s2) or len(s1) <= 0:
#         return false
#     return isSubString(s1+s1, s2)

# Simply joining s1 together allows us to make this check due to the
# following reason. Say s1 is "abcd" and s2 is "cdab". Then s1 + s1 is
# "abcdabcd" So if s2 is s1 rotated, we should be able to find it easily in s1.
