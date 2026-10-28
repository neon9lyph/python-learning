# list1 = [1, 2, 3]

# list1.append(4)
# print(list1)

# val = list1.pop()
# print(val)
# print(list1)
# print(len(list1))
# print(2 in list1)
# list1.remove(2)
# print(list1)

# # 本体是“,”
# tuple1 = 1, 2, 3
# print(tuple1)


nums = [0, 1, 2, 3, 4, 5]

nums[1:4]  # [1, 2, 3]：取索引 1 到 3
nums[:3]  # [0, 1, 2]：取前 3 个
nums[3:]  # [3, 4, 5]：从索引 3 取到末尾
nums[-2:]  # [4, 5]：取最后 2 个
nums[:-1]  # [0, 1, 2, 3, 4]：去掉最后一个

nums[::2]  # [0, 2, 4]：每隔一个取一个
nums[1::2]  # [1, 3, 5]：从索引 1 开始，每隔一个取一个
nums[::-1]  # [5, 4, 3, 2, 1, 0]：反转
nums[::-2]  # [5, 3, 1]：从末尾开始，每隔一个取一个

nums[:]  # [0, 1, 2, 3, 4, 5]：浅拷贝列表

import copy

a = ["123", "234"]
b = a

c = copy.deepcopy(a)

print(a, b, c)

a.pop()
print(a, b, c)
