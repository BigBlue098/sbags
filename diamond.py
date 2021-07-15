class A:
    def method(self):
        print("This method belongs to class A")

class B(A):
    def method(self):
        print("This class belongs to class B")

class C(A):
    def method(self):
        print("This class belongs to class C")

class D(B, C):
    pass


d = D()
d.method()
