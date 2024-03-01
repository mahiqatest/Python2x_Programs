score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("You got Grade A")
elif 80 <= score <= 89:
    print("You got Grade B")
elif 70 <= score <= 79:
    print("You got Grade C")
elif 60 <= score <= 69:
    print("You got Grade D")
elif 0 <= score <= 59:
    print("You got Grade F")
else:
    print("Invalid input")
