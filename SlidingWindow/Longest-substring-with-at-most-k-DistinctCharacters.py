# link : https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/


def solve_brute_force(string: str, k: int) -> int:
    longest_substring = float("-inf")

    # Generate all substrings
    for i in range(len(string)):
        distinct_character = set()
        for j in range(i, len(string)):
            ch = string[j]
            distinct_character.add(ch)
            if distinct_character.__len__() > k:
                distinct_character.remove(ch)
                longest_substring = max(longest_substring, (j - 1) - i + 1)
                break

        if distinct_character.__len__() == k and longest_substring == float("-inf"):
            longest_substring = max(longest_substring, len(string))

    if longest_substring == float("-inf"):
        return 0
    return longest_substring


def solve_two_pointer_sliding_window(string: str, k: int) -> int:
    longest_window = float("-inf")
    left_pointer: int = 0
    right_pointer: int = 0
    distinct_char_dict: dict = {}
    length = len(string)

    while right_pointer < length:
        if string[right_pointer] in distinct_char_dict:
            distinct_char_dict[string[right_pointer]] = (
                distinct_char_dict.get(string[right_pointer]) + 1
            )

        else:
            distinct_char_dict[string[right_pointer]] = 1

        # Check given condition
        # Shrinking the window until the dictionary is less than or equal to k
        while distinct_char_dict.keys().__len__() > k:
            distinct_char_dict[string[left_pointer]] = (
                distinct_char_dict.get(string[left_pointer]) - 1
            )
            if distinct_char_dict.get(string[left_pointer]) == 0:
                distinct_char_dict.pop(string[left_pointer])

            left_pointer += 1

        if distinct_char_dict.keys().__len__() <= k:
            longest_window = max(longest_window, right_pointer - left_pointer + 1)
        right_pointer += 1

    if longest_window == float("-inf"):
        return 0

    return longest_window


def longest_substring_k_distinct(string: str, k: int) -> int:
    # return solve_brute_force(string, k)
    return solve_two_pointer_sliding_window(string, k)


print(longest_substring_k_distinct("aaabbccd", 2))  # correct: 5
print(longest_substring_k_distinct("eceba", 2))  # correct: 3
print(longest_substring_k_distinct("aabbcc", 3))  # correct: 6
print(longest_substring_k_distinct("aaabbb", 3))  # correct: 0
print(longest_substring_k_distinct("araaci", 2))  # correct: 4
