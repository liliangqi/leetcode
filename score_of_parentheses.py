# ---------------------------------------------------------
# Title: Score of Parentheses
#
# Description:
#   Given a balanced parentheses string S, compute the score of the string
# based on the following rule:
#   1. () has score 1
#   2. AB has score A + B, where A and B are balanced parentheses strings.
#   3. (A) has score 2 * A, where A is a balanced parentheses string.
#
# Example 1:
# Input: "()"
# Output: 1
#
# Example 2:
# Input: "(())"
# Output: 2
#
# Example 3:
# Input: "()()"
# Output: 2
#
# Example 4:
# Input: "(()(()))"
# Output: 6
#
# Creating Date: Jul 30
# Latest Rectifying: Jul 30
# ---------------------------------------------------------


def solution1(string):
    """
    :type string: str
    :rtype: int
    """

    stack = []
    score = 0
    left = True  # `left` indicates the if former symbol is '('

    for p in string:
        if p == '(':
            stack.append(p)
            left = True
        else:
            stack.pop()
            if left:
                score += 2 ** len(stack)
                left = False

    return score


def main():

    string = '()'
    score = solution1(string)
    print('The score is', score)


if __name__ == '__main__':

    main()
