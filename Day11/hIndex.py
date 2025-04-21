from typing import List  
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_h = 0
        # 基础思路 每次循环 循环得到结果再与其他的值进行比对 用max存
        for i in range(1,len(citations)):
            if(citations[i]>max_h):
                