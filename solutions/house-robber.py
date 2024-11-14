'''
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
'''


class Robber:
    def __init__(self, street: list[int]):
        self.street = street
        self.robber_options = dict()

    def optimize_route(self):
        for house_number_lower in range(0, len(self.street)):
            for house_number_upper in range(0, len(self.street)):
                self.robber_options[sum(self.street[house_number_lower:house_number_upper:2])] = self.street[house_number_lower:house_number_upper:2]

        max_sum = max([key for key in self.robber_options])
        return self.robber_options[max_sum]


nums = [1, 2, 3, 1]
robby = Robber(nums)
print(robby.optimize_route())
