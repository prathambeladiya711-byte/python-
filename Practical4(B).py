def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate: "))
t = float(input("Enter time in years: "))

result = calculate_simple_interest(p, r, t)
print("Simple Interest:", result)
