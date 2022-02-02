number = 7


while True:
    user = input("Would you like to play? (Y/n): ")

    if user == "n":
        break

    user_num = int(input("Guess out number: "))
    if user_num == number:
        print("Correct!!!")
    elif number - user_num in (1, -1):
        print("You were off by one.")
    else:
        print("It's wrong :)")


#

friends = ["rolf", "raj", "loki"]

for friend in friends:
    print(f"{friend} is my friend.")

#

grades = [34, 56, 76, 89]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)

# sum()

grades = [34, 56, 76, 89]
total = sum(grades)
amount = len(grades)

print(total / amount)



   