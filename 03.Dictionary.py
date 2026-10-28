# a = {"key1": "value1"}
# print(a["key1"], a.get("key1"))

# a.update({"key2": "value2"})
# print(a)

# b = a | {"key3": "value3"}
# print(b)


# del a["key2"]
# print(a)


# d = b.pop("key4", "value4")
# print(b, d)

# print(a.keys(), a.values(), a.items())


student = {"name": "小明", "age": 18}

# 保存字典视图
keys_view = student.keys()
values_view = student.values()
items_view = student.items()

print(keys_view)  # dict_keys(['name', 'age'])
print(values_view)  # dict_values(['小明', 18])

# 修改字典
student["age"] = 20
student["city"] = "北京"
del student["name"]

# 不需要重新调用 keys()、values() 或 items()
print(keys_view)  # dict_keys(['age', 'city'])
print(values_view)  # dict_values([20, '北京'])
print(items_view)  # dict_items([('age', 20), ('city', '北京')])
