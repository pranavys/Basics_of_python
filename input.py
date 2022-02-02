name = input("Enter your name: ")

print(name)

size = input("sqfeet: ")
sqfeet = int(size)
sq_mtr = sqfeet / 10.8
print(f"{sqfeet} square feet is equal to {sq_mtr:.4f} square meter.")