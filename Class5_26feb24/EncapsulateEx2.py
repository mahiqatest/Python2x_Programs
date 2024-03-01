class Password:
    def __init__(self, password):
        # self.password = None
        self.__password = password
        self.public_var = 10

    def get_password(self, is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("Invalid Password")

    def set_password(self, password):
        if len(password) > 10:
            self.__password = password
            print("Set to correct", self.__password)
        else:
            print("Not allowed, weak password")


pwd = Password("test23232kd")
print(pwd.public_var)
pwd.get_password(True)
pwd.set_password("Mahitest012345")
