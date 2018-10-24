# ---------------------------------------------------------
# Title: Sort Characters by Frequency
#
# Description:
#   Given a string, sort it in decreasing order based on the frequency
# of characters.
#
# Example 1:
# Input: "tree"
# Output: "eert" or "eetr"
#
# Example 2:
# Input: "cccaaa"
# Output: "cccaaa" or "aaaccc"
#
# Example 3:
# Input: "Aabb"
# Output: "bbAa" or "bbaA"
#
# Creating Date: Oct 23
# Latest Rectifying: Oct 23
# ---------------------------------------------------------
import operator


def solution1(s):
    """Idea by myself."""

    # Count the frequency
    freq_dict = dict()
    for ch in s:
        if ch in freq_dict:
            freq_dict[ch] += 1
        else:
            freq_dict[ch] = 1

    chs = list(freq_dict.keys())
    frequecies = [freq_dict[ch] for ch in chs]

    # Sort the charachters by frequency
    freq_ind = [(freq, index) for index, freq in enumerate(frequecies)]
    sorted_ind = sorted(freq_ind, key=operator.itemgetter(0))[::-1]
    arg_sort = [item[1] for item in sorted_ind]
    sorted_chs = [chs[idx] for idx in arg_sort]

    return ''.join([ch * freq_dict[ch] for ch in sorted_chs])


def solution2(s):
    """Idea from the other guy."""

    chs = set(s)
    # Make a list of [count of char, char]
    counted_chs = [[s.count(c), c] for c in chs]
    counted_chs.sort(key=operator.itemgetter(0),
                     reverse=True)  # Descend sort, by list[i][0]
    return ''.join(t[1] * t[0] for t in counted_chs)  # Concate char * times


def main():

    s = 'tree'
    print(solution2(s))


if __name__ == '__main__':

    main()
