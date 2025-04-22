from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # 计算前缀积
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # 计算后缀积并更新结果
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer