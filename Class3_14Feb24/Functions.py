def say_hello(name):
    print("Hello folks!!", name)

say_hello("Rajesh")

def greet(name):
    print("Welcome ",name)

greet("Akshay")

def make_pizza(*toppings,base= "normal crust"):
    print(toppings)
    for topping in toppings:
        print (topping)

client1_akshay = make_pizza("paneer","swweet corn", "papperoni")
client2_rajesh = make_pizza("mushroom","non-veg")
