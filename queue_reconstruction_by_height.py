# ---------------------------------------------------------
# Title: Queue Reconstruction by Height
#
# Description:
#   Suppose you have a random list of people standing in a queue. Each person
# is described by a pair of integers (h, k), where h is the height of the
# person and k is the number of people in front of this person who have a
# height greater than or equal to h. Write an algorithm to reconstruct the
# queue.
#
# Example:
# Input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# Output: [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#
# Creating Date: Jun 19
# Latest Rectifying: Jun 19
# ---------------------------------------------------------


def solution1(people):
    """
    Idea from other guy
    ---
    :type people: list[list[int]]
    :rtype: list[list[int]]
    """

    heights = []
    grouped = {}

    for person in sorted(people):
        if person[0] in grouped:
            grouped[person[0]].append(person)
        else:
            grouped[person[0]] = [person]
            heights.append(person[0])

    output = []
    for height in sorted(heights, reverse=True):
        for person in grouped[height]:
            output.insert(person[1], person)

    return output


def main():

    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    output = solution1(people)
    print(output)


if __name__ == '__main__':

    main()
