from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        temp = 1  # 初始化 temp 为 1，因为至少有一个元素

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                temp = 1  # 重置 temp
            else:
                if temp < 2:
                    slow += 1
                    nums[slow] = nums[fast]
                    temp += 1

        return slow + 1