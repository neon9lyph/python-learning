class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.__sex = sex

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Sex: {self.__sex}")

    def get_sex(self):
        return self.__sex


student1 = Student("Alice", 20, "Female")
# student1.display_info()
# print(student1.name)  # 可以访问公有属性
# print(student1.get_sex())  # 通过公有方法访问私有属性


# 继承和多态
class Animal:
    def run(self):
        print("Animal is running...")


class Dog(Animal):
    pass
    # def run(self):
    #     print("Dog is running...")


class Cat(Animal):
    # 重写
    def run(self):
        print("Cat is running...")


def run_twice(animal):
    animal.run()
    animal.run()


dog = Dog()
cat = Cat()

dog.run()  # 输出: Dog is running...
cat.run()  # 输出: Cat is running...

print(isinstance(dog, Animal))  # 输出: True
print(isinstance(cat, Dog))  # 输出: false
run_twice(dog)  # 输出: Dog is running... Dog is running...
