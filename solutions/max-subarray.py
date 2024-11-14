'''
53. Maximum Subarray
Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


class Array:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.sums = dict()

    def largest_sum(self):
        if not self.sums:
            self._generate_sums()
        max_sum = self._max_sum()
        return self.sums[max_sum]

    def _max_sum(self):
        return max([key for key in self.sums])

    def _generate_sums(self):
        for i in range(0, len(self.nums)):
            for j in range(0, len(nums[i:])):
                self.sums[sum(nums[i:j])] = nums[i:j]


nums = [-2, 1, 0, 4, -7, 2, 1, -5, 4]
array = Array(nums)
print(array.largest_sum())
