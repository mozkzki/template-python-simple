from app_name.module1 import Module1


def main():
    user_name = input("user name: ")
    password = input("password: ")

    m1 = Module1()
    m1.method()

    result = login(user_name, password)
    print(result)


def login(user_name: str, password: str) -> str:
    print("login by {}....".format(user_name))
    return "done."


if __name__ == "__main__":
    main()
