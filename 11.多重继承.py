class A:
    def run(self):
        print("A run")


class B:
    def run(self):
        print("B run")

    def b():
        print("B b")


class C:
    def run(self):
        print("C run")

    def c():
        print("C c")


class D(A, B, C):
    pass


d = D()
print(f"Method Resolution Order (MRO) for class D: {dir(d)}")
d.run()  # This will call the run method from class A due to the method resolution
