# Single Inheritance

class Father:
    __private_villa = "Goa"
    gold = "5 kg"

    def drive_car(self):
        print("I have Lambo")

    def threeBHKFlat(self):
        print("3 Bhk flat")

    def private_villa_access(self, is_myson):
        if is_myson:
            print(self.__private_villa)


class Son(Father):
    pass


rishi = Son()
rishi.drive_car()
rishi.threeBHKFlat()
print(rishi.gold)
rishi.private_villa_access(True)

mmd = Father()
mmd.drive_car()
mmd.threeBHKFlat()
print(mmd.gold)

