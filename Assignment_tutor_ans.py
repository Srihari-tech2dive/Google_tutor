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