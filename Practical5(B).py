#Practical 5.2

n = int(input("Enter number of elements: "))

t = ()

for i in range(n):
    x = int(input("Enter value: "))
    t = t + (x,)

print("Tuple:", t)

# Using indexing
print("First element:", t[0])

# Using loop
print("Tuple elements:")
for x in t:
    print(x)
