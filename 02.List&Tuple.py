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

import copy

a = ["123", "234"]
b = a

c = copy.deepcopy(a)

print(a, b, c)

a.pop()
print(a, b, c)
