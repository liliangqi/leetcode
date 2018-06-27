# ---------------------------------------------------------
# Title: Single Number III
#
# Description:
#   Given an array of numbers nums, in which exactly two elements appear
# only once and all the other elements appear exactly twice. Find the two
# elements that appear only once.
#
# Example:
# Input: [1, 2, 1, 3, 2, 5]
# Output: [3, 5]
#
# Note:
#   1. The order of the result is not important. So in the above example,
# [5, 3] is also correct.
#   2. Your algorithm should run in linear runtime complexity. Could you
# implement it using only constant space complexity?
#
# Creating Date: Jun 27
# Latest Rectifying: Jun 27
# ---------------------------------------------------------


from collections import Counter


def solution1(nums):
    """
    Solution by myself
    ---
    Runtime: 48ms
    ---
    :type nums: list[int]
    :rtype: list[int]
    """
    repeated_nums = []
    num_set = set()

    for num in nums:
        if num in num_set:
            repeated_nums.append(num)
        else:
            num_set.add(num)

    return list(set(nums) - set(repeated_nums))


def solution2(nums):
    """
    Solotion from other guy
    ---
    Runtime: 40ms
    ---
    :type nums: list[int]
    :rtype: list[int]
    """
    res = []
    counts = Counter(nums)

    for i, v in counts.items():
        if v == 1:
            res.append(i)

    return res


def main():

    nums = [1, 2, 1, 3, 2, 5]
    output = solution1(nums)
    print(output)


if __name__ == '__main__':

    main()
