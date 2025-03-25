from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 笨办法 时间复杂度o（n） 空间复杂度 o（n）
        # count_dict = {}
        # for num in nums:
        #     if num in count_dict:
        #         count_dict[num] += 1
        #     else:
        #         count_dict[num] = 1
        #
        # for num, count in count_dict.items():
        #     if count > len(nums) / 2:
        #         return num

        # map_dict = {}  # 初始化字典
        # for i in range(len(nums)):
        #     if nums[i] not in map_dict:
        #         map_dict[nums[i]] = 1
        #     else:
        #         map_dict[nums[i]] += 1
        #     if map_dict[nums[i]] > len(nums) / 2:
        #         return nums[i]
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
