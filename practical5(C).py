student = {
    "name": "pratham",
    "age": 18,
    "course": "Python"
}

student["grade"] = "A"

print("Dictionary after insertion:", student)

print("Name:", student["name"])
print("Course:", student.get("course"))

del student["age"]

print("Dictionary after deletion:", student)