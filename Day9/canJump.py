from typing import List

class Solution:
    def canJump_dfs(self, nums: List[int]) -> bool:
        def dfs(position: int) -> bool:
            # 如果当前位置已经到达或超过了最后一个位置，返回True
            if position >= len(nums) - 1:
                return True
            # 如果当前位置的值为0，无法继续跳跃，返回False
            if nums[position] == 0:
                return False
            # 尝试从当前位置跳跃到每一个可能的位置
            for jump in range(1, nums[position] + 1):
                if dfs(position + jump):
                    return True
            return False
        
        return dfs(0)
    

    def canJump_cupidity(self, nums: List[int]) -> bool:
        # 初始化可以到达的最远位置
        max_reach = 0
        # 遍历数组中的每一个位置
        for i in range(len(nums)):
            # 如果当前位置超过了可以到达的最远位置，返回False
            if i > max_reach:
                return False
            # 更新可以到达的最远位置
            max_reach = max(max_reach, i + nums[i])
            # 如果可以到达或超过最后一个位置，返回True
            if max_reach >= len(nums) - 1:
                return True
        