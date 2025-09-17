#Mini-Assignment 4: The To-Do List Manager
tasks = [] 

while True:
  
    user_choice = input("\nEnter 'add', 'view', 'remove', or 'exit': ").lower()

    if user_choice == "add":
        new_task = input("What task do you want to add? ")
        tasks.append(new_task)
        print(f"'{new_task}' has been added to your list.")

    elif user_choice == "view":
        print("\n--- Your To-Do List ---")
        if not tasks: 
            print("Your to-do list is empty.")
        else:
            
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
        print("-----------------------")

    elif user_choice == "remove":
        if not tasks:
            print("Your list is already empty, nothing to remove.")
        else:
            print("Here are your current tasks:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")

            try:
                task_num_to_remove = int(input("Enter the number of the task to remove: "))
               
                if 1 <= task_num_to_remove <= len(tasks):
                    removed_task = tasks.pop(task_num_to_remove - 1)
                    print(f"'{removed_task}' has been removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")


    elif user_choice == "exit":
        print("Goodbye!")
        break 

    else:
        print("Invalid input. Please try again.")

# Mini-Assignment 4.5: The Simple Contact Book (Polished)
contacts = []
while True:
    user_choice = input("\nEnter 'add', 'view', 'search', or 'exit': ").lower()

    if user_choice == "add":
        name = input("Enter the person's name: ")
        phone_number = input("Enter the contact number: ")
        # Combine and add to the list
        contact_details = f"{name}:{phone_number}"
        contacts.append(contact_details)
        print(f"Added '{contact_details}' to contacts.")

    elif user_choice == "view":
        if not contacts:
            print("Your contact book is empty.")
        else:
            print("\n--- Your Contacts ---")
            for contact in contacts:
                print(contact)
            print("---------------------")

    elif user_choice == "search":
        search_name = input("Enter the name to search for: ")
        found_match = False
        for contact in contacts:
            if search_name.lower() in contact.lower():
                print(f"Found: {contact}")
                found_match = True
        
        if not found_match:
            print("Contact not found.")

    elif user_choice == "exit":
        print("Goodbye!")
        break
        
    else:
        print("Invalid input. Please try again.")

# --- Mini-Assignment 5 (Corrected Version) ---

# 1. Create the dictionary as requested in the assignment.
# "student_name" and "roll_number" are top-level keys.
report = {
    "student_name": "Rohan",
    "roll_number": 101,
    "subjects": {
        "Math": 85,
        "Science": 92,
        "English": 78,
        "History": 88
    }
}

# --- Print the static information ---
print("--- REPORT CARD ---")
# Access the top-level keys directly
print(f"Student Name: {report['student_name']}")
print(f"Roll Number:  {report['roll_number']}")
print("---------------------")
print("SUBJECT      MARKS")

# --- Loop through the nested 'subjects' dictionary ---
total_marks = 0
subject_dict = report["subjects"] # Get the inner dictionary first

for subject, marks in subject_dict.items():
    print(f"{subject:<13}{marks}") # The "<13" adds spacing to align the columns
    total_marks += marks # Add the marks to our total

# --- Calculate and print the final results ---
num_subjects = len(subject_dict)
average = total_marks / num_subjects

print("---------------------")
print(f"Total Marks:  {total_marks}")
print(f"Average:      {average:.2f}%") # :.2f formats the average to 2 decimal places
print("---------------------")

#Question 1: The User Profile Updater

user_profile = {
    "username": "coder_suresh",
    "email": "suresh@example.com",
    "location": {
        "city": "Chennai",
        "country": "India"
    }
}

# 1. Access the nested "city" key
print(f"The user's city is: {user_profile['location']['city']}")

# 2. Update the email (Your code was perfect here)
user_profile["email"] = "suresh.dev@example.com"

# 3. Add skills (Your code was perfect here too)
user_profile["skills"] = ["Python", "Data Structures", "SQL"]

# 4. Print the final result
print("\n--- Updated Profile ---")
print(user_profile)

#Question 2: The Inventory Value Calculator

inventory = {
    "Laptop": {"price": 80000, "quantity": 10},
    "Mouse": {"price": 1500, "quantity": 50},
    "Keyboard": {"price": 2500, "quantity": 30}
}

total_value = 0 # Use a descriptive variable name

# We only need ONE loop to go through the main inventory.
# 'item_details' will hold the inner dictionary like {"price": 80000, "quantity": 10}
for item, item_details in inventory.items():
    # Access the price and quantity from the inner dictionary
    price = item_details["price"]
    quantity = item_details["quantity"]
    
    # Calculate the value for the current item and add to the total
    value = price * quantity
    total_value += value
    
print(f"The total value of the inventory is: {total_value}")

#Question 3: The Student Search (Challenge)

students = [
    {"id": 101, "name": "Kavya", "grade": 88},
    {"id": 102, "name": "Vijay", "grade": 92},
    {"id": 103, "name": "Lakshmi", "grade": 75}
]

user_choice = int(input("Enter student id to search for: "))
student_found = False # Our "flag" variable

# ONE loop is all we need
for student in students:
    # Directly access the "id" key and check it
    if student["id"] == user_choice:
        print(f"Found Student: {student['name']}, Grade: {student['grade']}")
        student_found = True # Set the flag to True
        break # Exit the loop immediately since we found the student

# This check happens only ONCE, after the loop is finished
if not student_found:
    print("Student not found.")
    