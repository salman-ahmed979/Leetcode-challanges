# link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''

Dict = {
    character = index
}


'''
def lengthOfLongestSubstring(self, s: str) -> int:
    left_pointer = 0
    max_length_substring = float("-inf")
    charIndexMap: dict = {}

    for right_pointer in range(len(s)):
        if s[right_pointer] in charIndexMap:
            # If the left pointer is at higher level and some value already exist in the dict
            if left_pointer > charIndexMap.get(s[right_pointer]):
                charIndexMap[s[right_pointer]] = right_pointer
            else:
                left_pointer = charIndexMap.get(s[right_pointer]) + 1
                charIndexMap.pop(s[right_pointer])

        charIndexMap[s[right_pointer]] = right_pointer

        max_length_substring = max(
            max_length_substring, right_pointer - left_pointer + 1
        )

    if max_length_substring == float("-inf"):
        return 0

    return max_length_substring
