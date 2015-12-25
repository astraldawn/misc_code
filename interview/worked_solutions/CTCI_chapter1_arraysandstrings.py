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


test_one_five()
