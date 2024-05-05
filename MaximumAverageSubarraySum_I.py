# link: https://leetcode.com/problems/maximum-average-subarray-i/description/

def findMaxAverage(self, nums: List[int], k: int) -> float:
        # best approach
        # j = 0
        # max_avg = sum_avg = sum(nums[:k])
        # for i in range(k, len(nums)):
        #     sum_avg = sum_avg + nums[i] - nums[j]
        #     j += 1
        #     max_avg = max(max_avg, sum_avg)
        # return max_avg / k

        # another approach but not good:
        max_avg = None
        start = 0
        summation = 0
        window = 0
        for i in range(len(nums)):
            summation += nums[i]
            window += 1
            if window == k:
                if max_avg is None:
                    max_avg = summation
                else:
                    max_avg = max(max_avg, summation)
                summation -= nums[start]
                start += 1
                window -= 1
        return max_avg / k

        # first approach
        # pointer to note: here was the condition to compare length of num with k upon which after removal we achieve 881 ms 
        '''
        left_pointer = 0
        right_pointer = k-1
        initial_iteration = True
        summation = 0
        max_average = float('-inf')
        while right_pointer < len(nums):
                if initial_iteration:
                    for i in range(right_pointer + 1):
                        summation += nums[i]
                    initial_iteration = False
                else:
                    summation += nums[right_pointer]
                max_average = max(max_average, summation)
                summation -= nums[left_pointer]
                left_pointer += 1
                right_pointer += 1
        return max_average / k
        '''