from main.my.sub.module2 import Module2


class Module1:
    def method(self) -> None:
        print("module1's method called.")
        m2 = Module2()
        m2.method()
