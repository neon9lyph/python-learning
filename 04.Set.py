# 集合 set：元素不重复、无序，不能通过下标访问。
# 下面用 sorted() 展示数字集合，方便观察结果；排序后得到的是列表。

# print("\n1. 创建集合与去重")
# numbers = {3, 1, 2, 2, 3}
# print("numbers 的类型：", type(numbers))  # <class 'set'>
# print("重复元素只保留一份：", sorted(numbers))  # [1, 2, 3]
# print("列表转集合：", sorted(set([1, 1, 2, 3])))  # [1, 2, 3]

# empty_set = set()
# print("set() 的类型：", type(empty_set))  # <class 'set'>
# print("{} 的类型：", type({}))  # <class 'dict'>，空花括号创建的是字典


# print("\n2. 添加与删除元素")
# numbers.add(4)
# numbers.add(4)  # 添加已有元素不会产生重复项
# numbers.update([4, 5, 6])  # 将可迭代对象中的元素逐个加入集合
# print("添加后：", numbers, sorted(numbers))  # [1, 2, 3, 4, 5, 6]


# numbers.remove(6)  # 删除指定元素；元素不存在时会抛出 KeyError
# numbers.discard(99)  # 元素不存在时也不会报错
# print("删除后：", sorted(numbers))  # [1, 2, 3, 4, 5]

# try:
#     numbers.remove(99)
# except KeyError:
#     print("remove(99)：元素不存在，触发 KeyError")

# popped = numbers.pop()  # 删除并返回任意一个元素，不保证是最小值或最后加入的值
# print("pop() 删除的元素：", popped)
# print("剩余元素：", sorted(numbers))
# numbers.clear()
# print("清空后：", numbers)  # set()


# print("\n3. 成员判断、长度与遍历")
# fruits = {"苹果", "香蕉", "橙子"}
# print("苹果是否在集合中：", "苹果" in fruits)  # True
# print("梨是否不在集合中：", "梨" not in fruits)  # True
# print("元素数量：", len(fruits))  # 3
# for fruit in sorted(fruits):  # 排序后遍历，使展示顺序固定
#     print("水果：", fruit)


# print("\n4. 集合运算")
# a = {1, 2, 3}
# b = {3, 4, 5}
# print("并集（所有元素）：", sorted(a | b))  # [1, 2, 3, 4, 5]
# print("交集（共同元素）：", sorted(a & b))  # [3]
# print("差集（在 a 中但不在 b 中）：", sorted(a - b))  # [1, 2]
# print("反向差集（在 b 中但不在 a 中）：", sorted(b - a))  # [4, 5]
# print("对称差集（只在其中一个集合中）：", sorted(a ^ b))  # [1, 2, 4, 5]
# print("运算后 a 保持不变：", sorted(a))  # [1, 2, 3]
# # 对应的方法：union()、intersection()、difference()、symmetric_difference()
# # 如果需要修改原集合，可以使用 a |= b、a &= b 等原地运算。


# print("\n5. 集合之间的关系")
# small = {1, 2}
# large = {1, 2, 3}
# print("small 是 large 的子集：", small <= large)  # True
# print("small 是 large 的真子集：", small < large)  # True
# print("large 是 small 的超集：", large >= small)  # True
# print("相同集合不是真子集：", small < {1, 2})  # False
# print("是否没有共同元素：", small.isdisjoint({3, 4}))  # True
# print("相等与书写顺序无关：", {1, 2} == {2, 1})  # True


# print("\n6. 集合推导式")
# even_squares = {n * n for n in range(6) if n % 2 == 0}
# print("0 到 5 中偶数的平方：", sorted(even_squares))  # [0, 4, 16]


# print("\n7. 元素类型与不可变集合")
# # 集合元素必须可哈希：整数、字符串、只包含可哈希元素的元组等可以加入。
# # 列表、字典、普通集合不可哈希，不能作为集合元素。
# points = {(1, 2), (3, 4)}
# print("元组可以作为集合元素：", sorted(points))
# try:
#     points.add([5, 6])
# except TypeError:
#     print("添加列表会触发 TypeError：列表不可哈希")

# fixed = frozenset({1, 2, 3})  # 不可变集合，不能调用 add() 或 remove()
# nested = {fixed}  # frozenset 可哈希，可以成为另一个集合的元素
# print("不可变集合也支持交集：", sorted(fixed & {2, 3, 4}))  # [2, 3]
# print("包含不可变集合的集合长度：", nested, len(nested))  # 1


# 练习：先自己预测结果，再取消下面代码的注释运行。
python_students = {"小明", "小红", "小李"}
java_students = {"小红", "小王"}
print("两门课都学：", python_students & java_students)  # {"小红"}
print("只学 Python：", python_students - java_students)  # {“小明", "小李"}
print(
    "至少学一门：", python_students | java_students
)  # {"小明", "小红", "小李", "小王"}
