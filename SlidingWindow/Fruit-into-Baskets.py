# link: https://leetcode.com/problems/fruit-into-baskets/
# predecessor: Longest-substring-with-at-most-k

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left_pointer = 0
        distinct_fruits: dict = {}
        max_fruits = float("-inf")

        for right_pointer in range(len(fruits)):
            if fruits[right_pointer] in distinct_fruits:
                distinct_fruits[fruits[right_pointer]] = distinct_fruits.get(fruits[right_pointer]) + 1
            else:
                distinct_fruits[fruits[right_pointer]] = 1
            
            while distinct_fruits.keys().__len__() > 2:
                distinct_fruits[fruits[left_pointer]] = distinct_fruits.get(fruits[left_pointer]) - 1
                if distinct_fruits.get(fruits[left_pointer]) == 0:
                    distinct_fruits.pop(fruits[left_pointer])
                left_pointer += 1
            
            if distinct_fruits.keys().__len__() <= 2:
                max_fruits = max(max_fruits, right_pointer - left_pointer + 1)

        if max_fruits == float("-inf"):
            return 0
        return max_fruits 