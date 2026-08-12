# Create a list of n integers
n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)

print("Original list:", numbers)

# Insertion operation
position = int(input("Enter position for insertion: "))
value = int(input("Enter value to insert: "))

numbers.insert(position, value)
print("List after insertion:", numbers)

# Deletion operation
position = int(input("Enter position for deletion: "))

if 0 <= position < len(numbers):
    deleted_value = numbers.pop(position)
    print("Deleted value:", deleted_value)
    print("List after deletion:", numbers)
else:
    print("Invalid position")