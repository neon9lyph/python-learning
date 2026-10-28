student = ["Alice1", "Bob", "Charlie", "David", "Eva"]

# 报错
# for index,name in student:
#     print(f"Student {index}：{name}")


for index, name in enumerate(student, start=1):
    print(f"Student {index}: {name}")

if student[0] == "Alice":
    print("The first student is Alice.")
elif student[1] == "Bob":
    print("The second student is Bob.")
else:
    print("The first student is neither Alice nor Bob.")


a = {"type": "search", "keywords": ["python", "loops", "enumerate"]}

match a:
    case {"type": "search", "keywords": kwd_list}:
        print(f"{kwd_list}")
