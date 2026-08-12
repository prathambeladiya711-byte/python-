<<<<<<< HEAD
choice = input("Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ")

temp = float(input("Enter temperature: "))

if choice == "C":
    f = (temp * 9/5) + 32
    print("Fahrenheit =", f)

elif choice == "F":
    c = (temp - 32) * 5/9
    print("Celsius =", c)

else:
=======
choice = input("Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ")

temp = float(input("Enter temperature: "))

if choice == "C":
    f = (temp * 9/5) + 32
    print("Fahrenheit =", f)

elif choice == "F":
    c = (temp - 32) * 5/9
    print("Celsius =", c)

else:
>>>>>>> 74749572667462e54cbe4527c6342a979a9c1499
    print("Invalid choice")