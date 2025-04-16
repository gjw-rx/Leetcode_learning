from typing import List  
class Solution:
    def jump(self, nums: List[int]) -> int:
        # # dfs 方法时间复杂度太高  
        # min_count = float('inf')  
        # n = len(nums)  
        # def dfs(pos: int, count: int):  
        #     nonlocal min_count  
        #     if pos >= n - 1:  
        #         min_count = min(min_count, count)  
        #         return True  
        #     if count >= min_count:  
        #         return False  
        #     if nums[pos] == 0:  
        #         return False  
        #     for i in range(1, nums[pos] + 1):  
        #         dfs(pos + i, count + 1)  
        # dfs(0, 0)
        # return min_count


        # 数组长度小于2 直接返回
        n = len(nums)
        if n<2:
            return 0
        # 初始最大的距离为nums[0] 能到的最远终点是nums[0] 跳跃的次数至少需要一次
        max_position = nums[0]
        end = nums[0]
        jumps = 1
        for i in range(1,n):
            # 如果当前位置超过了max_position 说明无法到达
            if i > max_position:
                return -1
            # 最大距离更新为从当前位置开始能到的最大距离
            max_position = max(max_position, i + nums[i])
            # 从第i出发已经到达最远距离
            if i == end:
                # 还可以继续出发 说明此时还需要再跳一步
                if i < n-1:
                    jumps += 1
                    end = max_position
                # 此时已经无法继续出发 直接跳出循环
                else:
                    break
        return jumps




        
