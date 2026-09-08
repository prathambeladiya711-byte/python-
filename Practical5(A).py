# Create a list
n = int(input("Enter n: "))

a = []
for i in range(n):
    a.append(int(input("Enter number: ")))

print("Original list:", a)

# Insertion
pos = int(input("Enter position: "))
value = int(input("Enter value: "))
a.insert(pos, value)

print("After insertion:", a)

# Deletion
pos = int(input("Enter position to delete: "))
a.pop(pos)

print("After deletion:", a)
