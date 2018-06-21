# ---------------------------------------------------------
# Title: Palindromic Substrings
#
# Description:
#   Given a string, your task is to count how many palindromic substrings in
# this string.
#   The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
#
# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
# Creating Date: Jun 21
# Latest Rectifying: Jun 21
# ---------------------------------------------------------


def solution1(s):
    """
    Inefficient solution by myself
    ---
    Runtime: 628ms
    ---
    :type s: str
    :rtype: int
    """

    count = len(s)
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            cur_slice = s[i:j]
            if cur_slice == cur_slice[::-1]:
                count += 1

    return count


def solution2(s):
    """
    Solution from other guy
    ---
    Runtime: 48ms
    ---
    :type s: str
    :rtype: int
    """

    # manacher, find Z
    s = '^#' + '#'.join(s) + '#$'
    zz = [1] * len(s)
    center, right = 0, 0
    for i in range(len(s) - 1):  # Note
        if i < right:
            i_mirror = 2 * center - i
            zz[i] = min(zz[i_mirror], right - i + 1)
        while s[i + zz[i]] == s[i - zz[i]]:
            zz[i] += 1
        if i + zz[i] - 1 > right:
            center, right = i, i + zz[i] - 1

    # sum Z
    return sum(z // 2 for z in zz)


def main():

    s = 'abc'
    count = solution2(s)
    print(count)


if __name__ == '__main__':

    main()
