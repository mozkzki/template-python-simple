from app_name.module1 import Module1


def main():
    user_name = input("user name: ")
    password = input("password: ")
    result = login(user_name, password)
    print(result)


def login(user_name: str, password: str) -> str:
    print("login by {}....".format(user_name))
    m1 = Module1()
    m1.method()
    return "call module1 done."


if __name__ == "__main__":
    main()
