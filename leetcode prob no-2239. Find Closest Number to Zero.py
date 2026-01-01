class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_number = nums[0]
        for i in nums:
            if abs(i) < abs(closest_number):
                closest_number = i

        if closest_number < 0 and abs(closest_number) in nums:
            return abs(closest_number)
        else:
            return closest_number
