
class Solution(object):
    def missing_ranges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        def getRange(lower, upper):
            if lower == upper:
                return "{}".format(lower)
            else:
                return "{}->{}".format(lower, upper)
        ranges = []
        pre = lower - 1
        
        for i in range(len(nums) + 1):
            if i == len(nums):
                cur = upper + 1
            else:
                cur = nums[i]
            if cur - pre >= 2:
                ranges.append(getRange(pre + 1, cur - 1))
                
            pre = cur
            
        return ranges


if __name__ == "__main__":
    print(Solution().missing_ranges([0, 1, 3, 50, 75], 0, 99))
