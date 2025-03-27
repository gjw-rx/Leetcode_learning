from typing import List
def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    nums_new = [0] * (n+k)
    for i in range(n):
        nums_new[i+k] = nums[i]

    for i in range(n+k):
        if(i>=n):
            nums_new[i%n] = nums_new[i]
    for i in range(n):
        nums[i] = nums_new[i]