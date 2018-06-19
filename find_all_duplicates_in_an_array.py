# ---------------------------------------------------------
# Title: Find All Duplicates in an Array
#
# Description:
#   Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
# appear twice and others appear once.
#   Find all the elements that appear twice in this array.
#   Could you do it without extra space and in O(n) runtime?
#
# Example:
# Input: [4, 3, 2, 7, 8, 2, 3, 1]
# Output: [2, 3]
#
# Creating Date: Jun 19
# Latest Rectifying: Jun 19
# ---------------------------------------------------------


def solution1(nums):
    """
    Inefficient solution written by myself
    ---
    :type nums: list[int]
    :rtype: list[int]
    """
    repeated_nums = []
    for i, num in enumerate(nums):
        if num in nums[:i]:
            repeated_nums.append(num)

    return repeated_nums


def solution2(nums):
    """
    Efficient solution written by other guy
    ---
    :type nums: list[int]
    :rtype: list[int]
    """
    output = []

    for num in nums:
        # Same number in the array must conduct to the same index
        # And we should note that the number is always between 1 and n
        idx = abs(num) - 1

        if nums[idx] < 0:
            output.append(idx + 1)

        nums[idx] *= -1

    return output


def main():

    lst = [4, 3, 2, 7, 8, 2, 3, 1]
    results = solution2(lst)
    print(results)


if __name__ == '__main__':

    main()
