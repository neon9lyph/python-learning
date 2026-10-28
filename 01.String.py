# text = "apple banana apple"

# print(text.replace("apple", "orange"))
# # orange banana orange

# print(text.replace("apple", "orange", 1))
# # orange banana apple

# print(text)
# # apple banana apple


# text = "banana"
# # 索引： 012345

# print(text.find("an"))  # 1
# print(text.find("apple"))  # -1
# print(text.find("an", 2))  # 3，从索引 2 开始查找
# print(text.find("na", 2, 4))  # 3


# text = "banana"

# print(text.find("an"))  # 1，第一次出现
# print(text.rfind("an"))  # 3，最后一次出现
# print(text.rfind("x"))  # -1


# text = "一堆废话{'fruit': 'banana', 'color': 'yellow'}夹杂着json"

# start = text.find("{")
# end = text.rfind("}") + 1
# print(text[start:end])  # {'fruit': 'banana', 'color': 'yellow'}


score = 95
print(f"{score=}")  # 95

price = 3.12521
print(f"{price:.2f}")

count = 112312312
print(f"{count:,}")
