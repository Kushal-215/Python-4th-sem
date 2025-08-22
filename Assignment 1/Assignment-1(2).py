#Simple Form


name = input("Enter your name")
age = int(input("Enter your age"))
height = float(input("Enter your Height"))
country = input("Which country are you from?")
print("Hello "+name.upper())
print("Your age is", age)
print(f"Your height is {height :.2f} feet")
print("You are from", country.title())
print(f"Your nickname is {name.upper()[0:2]}"+f"{name.upper()[-2:]}")

