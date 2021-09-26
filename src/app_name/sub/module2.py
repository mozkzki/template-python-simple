from app_name.cls_sample import Owner, Dog


class Module2:
    def method(self) -> None:
        print("module2's method called.")

        owner = Owner("Zagitova", 17, "rusia")
        dog = Dog("Masaru", owner)
        dog.show()
