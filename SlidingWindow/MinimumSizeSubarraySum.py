# link : https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def update_min_subarray(self, min_subarray: int, min_length: int) -> int:
        if min_subarray == 0:
            min_subarray = min_length
        else: 
            min_subarray = min(min_subarray, min_length)
        return min_subarray
    

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_start = 0
        summation = 0
        min_window = float('inf')
        
        for end in range(len(nums)):
            summation += nums[end]

            while summation >= target:
                min_window = min(min_window, end - window_start + 1)
                summation -= nums[window_start]
                window_start += 1
        
        if min_window == float('inf'):
            return 0
        
        return min_window


    def minSubArrayLen_TwoPointer(self, target: int, nums: List[int]) -> int:
        left_pointer = 0
        right_pointer = 0
        summation = 0
        min_subarray = 0

        while right_pointer < len(nums):
            summation += nums[right_pointer]

            if summation >= target:
                min_subarray = self.update_min_subarray(min_subarray, right_pointer - left_pointer + 1)
	
	# shrinking part
                while left_pointer < right_pointer:
                    summation -= nums[left_pointer]
                    left_pointer += 1
                    if summation >= target:
                        min_subarray = self.update_min_subarray(min_subarray, right_pointer - left_pointer + 1)
                    else:
                        break

            right_pointer += 1
            check_window_size = right_pointer - left_pointer + 1
            if check_window_size > min_subarray and min_subarray != 0:
                summation -= nums[left_pointer]
                left_pointer += 1 
        
        return min_subarray 