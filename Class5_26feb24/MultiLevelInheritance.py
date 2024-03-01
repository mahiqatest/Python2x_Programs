# Multilevel Inheritance

class Grandfather:

    # __init__ is called a constructor
    def __init__(self):
        print("automatically called when object created")
    def home(self):
        print("2BHk")


class Father(Grandfather):
    def home2(self):
        print("3Bhk")


class Son(Father):
    def home3(self):
        print("4Bhk")


vicky = Son()
vicky.home()
vicky.home2()
vicky.home3()

mmd = Father()
mmd.home()
mmd.home2()

gkd = Grandfather()
gkd.home()

