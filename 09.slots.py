class Student:
    __slots__ = ("age", "name")


stu1 = Student()
stu1.age = 20
stu1.name = "John"
stu1.sex = "man"  # AttributeError: 'Student' object has no attribute 'sex'
