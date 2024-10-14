def password_protector(fun):
    def wrapper():
        password = input("Enter your password: ")
        if password == "chotu":
            fun()
        else:
            print("User you entered wrong password")

    return wrapper

@password_protector
def secrete_msg():
    print("I love India And Travelling with my bike me being me")

secrete_msg()