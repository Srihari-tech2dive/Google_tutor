# A dictionary representing a student
student = {
    "name": "Priya",
    "id_number": 408,
    "major": "Computer Science",
    "courses": ["Python Programming", "Data Structures", "Web Development"]
}
# This would cause an error because the key 'age' does not exist:
# print(student['age'])

# This is safe and will not cause an error:
print(student.get("age")) # Output: None
# Modifying an existing value
student["major"] = "Electrical Engineering"

# Adding a new key-value pair
student["year"] = 3

print(student)
for key, value in student.items():
    print(f"-> {key}: {value}")