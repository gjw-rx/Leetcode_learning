import random
from typing import List

class RandomizedSet:

    def __init__(self):
        # 初始化一个列表用于存储元素
        self.nums: List[int] = []
        # 初始化一个字典用于存储元素及其在列表中的索引
        self.val_to_index: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        # 如果元素已经存在，返回False
        if val in self.val_to_index:
            return False
        # 如果元素不存在，将其添加到列表末尾，并在字典中记录其索引
        self.val_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        # 如果元素不存在，返回False
        if val not in self.val_to_index:
            return False
        # 获取要删除元素的索引
        index = self.val_to_index[val]
        # 将列表末尾的元素移动到要删除元素的位置
        last_val = self.nums[-1]
        self.nums[index] = last_val
        self.val_to_index[last_val] = index
        # 删除列表末尾的元素
        self.nums.pop()
        # 删除字典中的元素
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        # 随机返回列表中的一个元素
        return random.choice(self.nums)

# 示例用法
if __name__ == "__main__":
    randomized_set = RandomizedSet()
    print(randomized_set.insert(1))  # 返回 True
    print(randomized_set.remove(2))  # 返回 False
    print(randomized_set.insert(2))  # 返回 True
    print(randomized_set.getRandom())  # 返回 1 或 2
    print(randomized_set.remove(1))  # 返回 True
    print(randomized_set.getRandom())  # 返回 2