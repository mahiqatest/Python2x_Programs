# Multiple inheritance achieved in python by method resolution order passed in arguments
# first argument will take preference passed in class level

class Father:
    def home(self):
        return "Father's home"

class Mother:
    def home(self):
        return "Mother's home"

# class Son(Father, Mother):
#     pass

class Son(Mother, Father):
    pass

rishi = Son()
print(rishi.home())