# ---------------------------------------------------------
# Title: Find All Duplicates in an Array
#
# Description:
#   Given a sorted array consisting of only integers where every element
# appears twice except for one element which appears once. Find this single
# element that appears only once.
#
# Example 1:
# Input: [1, 1, 2, 3, 3, 4, 4, 8, 8]
# Output: 2
#
# Example 2:
# Input: [3, 3, 7, 7, 10, 11, 11]
# Output: 10
#
# Note: Your solution should run in O(log n) time and O(1) space.
#
# Creating Date: Jun 20
# Latest Rectifying: Jun 20
# ---------------------------------------------------------


def solution1(nums):
    """
    Solution by myself
    ---
    :type nums: list[int]
    :rtype nums: int
    """

    for i in range(0, len(nums), 2):
        try:
            if nums[i] != nums[i + 1]:
                return nums[i]
        # Consider the condition that the single num is the last one
        except IndexError:
            return nums[i]


def main():

    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    output = solution1(nums)
    print(output)


if __name__ == '__main__':

    main()
