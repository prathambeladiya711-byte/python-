n = int(input("Enter the number of elements: "))

elements = []

for i in range(n):
    value = input(f"Enter element {i + 1}: ")
    elements.append(value)

my_tuple = tuple(elements)

print("\nTuple:", my_tuple)

print("\nAccessing elements using indexing:")
for i in range(len(my_tuple)):
    print("Index", i, ":", my_tuple[i])

print("\nAccessing elements using looping:")
for element in my_tuple:
    print(element)