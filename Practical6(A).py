
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

concatenated = str1 + " " + str2
print("\nConcatenated String:", concatenated)

print("Length of first string:", len(str1))
print("Length of second string:", len(str2))

print("Uppercase:", concatenated.upper())
print("Lowercase:", concatenated.lower())
print("Title Case:", concatenated.title())

start = int(input("\nEnter starting index for substring: "))
end = int(input("Enter ending index for substring: "))

print("Extracted Substring:", concatenated[start:end])