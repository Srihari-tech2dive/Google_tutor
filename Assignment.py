#Mini-Assignment 3: Loops and Logic Challenges 

#Question 1: The FizzBuzz Challenge

for i in range(1, 101): # Loop from 1 to 100
    # Condition 1: Is it a multiple of BOTH 3 and 5?
    # We check this first because it's the most specific.
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Condition 2: If not, is it a multiple of 3?
    elif i % 3 == 0:
        print("Fizz")
    # Condition 3: If not, is it a multiple of 5?
    elif i % 5 == 0:
        print("Buzz")
    # Condition 4: If none of the above are true, just print the number
    else:
        print(i)
        
#Question 2: The Input Validator
while(True):
  number=int(input("Enter the no. :"))  
  if number>0 :
    print(f"Success! {number} is a positive number.")
  else:
    break

#Question 3: The Summation Challenge
sum=0
n=int(input("Enter the no. :"))
for i in range(1,n+1):
  sum+=i
print(sum)


#Mini-Assignment 4: The To-Do List Manager

tasks = [ ]
menu_list=["add","view","remove","exit"]
while True :
    menu =input("Enter any one: add,\nview,\nremove,\nexit:\n").lower()
    for i in menu:
        if menu=="add":
            new=input("Enter new task:")
            tasks.append(new)
        elif menu=="view":
            for t in tasks:
                if tasks==0:
                    print("Your to-do list is empty")
                else:
                    print(t)
        elif menu=="remove":
            print("The tasks are",tasks)
            delete=int(input("The task you want to remove(say the position of it):"))
            if delete<0 or delete>=len(tasks):
                print("Invalid position")
            else:
                tasks.remove(delete)
        elif menu=="exit":
            break
        else:
            print("Invalid input")



#Mini-Assignment 4.5: The Simple Contact Book

contacts=[ ]
while True:
  user_choice = input("\nEnter 'add', 'view', 'search', or 'exit': ").lower()
  if user_choice=="add":
    name=input("Enter the person name:")
    phone_number=input("Enter the contact number:")
    combine=f"{name}:{phone_number}"
    print(combine)
    contacts.append(combine)
    # break
  elif user_choice=="view":
    if not contacts:
      print("Your contact book is empty.")
      # break
    else:
      for i in contacts:
        print(i,"\n")
  elif user_choice=="search":
    search_name=input("Enter the name to search:")
    for n in contacts:
      if n==search_name:
        print(f"Found:{search_name}")
      else:
        print("Contact not found")
  elif user_choice=="exit":
    print("Thanks")
    break
  else:
    print("Invalid input")

#Mini-Assignment 4.7: The Simple Expense Tracker

expenses =[ ]

while True:
  user_choice = input("\nEnter 'add', 'show', or 'exit': ").lower()
  if user_choice=="add":
    # expense_amount=float(input("Enter the amount:"))
    try:
      expense_amount = float(input("Enter the amount: "))
      expenses.append(expense_amount)
      print(f"Added expense: ${expense_amount:.2f}")
    except ValueError:
      print("Invalid input. Please enter a number.")
  elif user_choice=="show":
    if not expenses:
      print("You have no expenses yet.")
    else:
      print("--- Your Expenses ---")
      total=0
      for i in expenses:
        print(i)

        total+=i
      print(f"Total:${total}")
  elif user_choice=="exit":
    print("Goodbye!")
    break
  else:
    print("Invalid input")

#Mini-Assignment 5: The Student Report Card

report={
    "reports":{
    "student_name": "Rohan",
    "roll_number": 101},
    "subjects":{
              "Math": 85,
              "Science": 92,
              "English": 78,
              "History": 88
            }
}
print("--- REPORT CARD ---")
print("Student Name:",report.get("student_name"))
print("Roll Number:",report.get("roll_number"),"\n---------------------\n")
for key,value in report.subjects.items():
  print("c")

#Question 1: The User Profile Updater
user_profile = {
    "username": "coder_suresh",
    "email": "suresh@example.com",
    "location": {
        "city": "Chennai",
        "country": "India"
    }
}
print(user_profile["location"])
user_profile["email"]="suresh.dev@example.com"
user_profile["skills"]=["Python", "Data Structures","SQL"]
print(user_profile)

#Question 2: The Inventory Value Calculator
inventory = {
    "Laptop": {"price": 80000, "quantity": 10},
    "Mouse": {"price": 1500, "quantity": 50},
    "Keyboard": {"price": 2500, "quantity": 30}
}
total=0
add_dict1=inventory["Laptop"]
add_dict2=inventory["Mouse"]
add_dict3=inventory["Keyboard"]

for price, quantity in add_dict1.items():
  for price,quantity in add_dict2.items():
    for price,quantity in add_dict3.items():

      print(f"{price}:{quantity}")
      value=price*quantity
      
      total+=value
print("The total value of the inventory is:",total)

#Question 3: The Student Search (Challenge)
students = [
    {"id": 101, "name": "Kavya", "grade": 88},
    {"id": 102, "name": "Vijay", "grade": 92},
    {"id": 103, "name": "Lakshmi", "grade": 75}
]

user_choice=int(input("Enter id:"))

for dictionary in students:
    print(f"Processing dictionary: {dictionary}")
    for key, value in dictionary.items():
        # print(f"  Key: {key}, Value: {value}")
        cc=dictionary["id"]
        if user_choice==cc:
          print("Found")
          break
        else:
          print("Not found")

#Question 1: Student Averages

class_grades = {
    "Amit": {"Math": 88, "Science": 92, "History": 85},
    "Priya": {"Math": 95, "Science": 91, "History": 93},
    "Rahul": {"Math": 78, "Science": 82, "History": 80}
}
value=0

for name, subject_details in class_grades.items():
   
    sub = subject_details["Math"]
    sub2 = subject_details["Science"]
    
    sub3 = subject_details["History"]
    val=(sub+sub2+sub3)/3
    
    print(f"{name} average score is: {val}")

#Question 2: Product Filter

products = [
    {"name": "Laptop", "category": "Electronics", "price": 80000},
    {"name": "T-Shirt", "category": "Apparel", "price": 1200},
    {"name": "Mouse", "category": "Electronics", "price": 1500},
    {"name": "Jeans", "category": "Apparel", "price": 2500},
    {"name": "Monitor", "category": "Electronics", "price": 15000}
]

user_choice = input("Enter the category to filter for: ").lower()

item_found = False

for item in products:
    if item["category"].lower() == user_choice:
        print(f"Found item: {item['name']}, Price: {item['price']}")
        item_found = True
      

if not item_found:
    print(f"No items found in the category '{user_choice}'.")

#Question 3: Employee Raise (Challenge)

employees = [
    {"id": 1, "name": "Sanjay", "department": "IT", "salary": 60000},
    {"id": 2, "name": "Meera", "department": "HR", "salary": 50000},
    {"id": 3, "name": "Vikram", "department": "IT", "salary": 65000}
]

# user_choice = input("Enter the department to filter for: ").lower()

department_found = False

for dept in employees:
    if dept["department"] == "IT":
        # print(f"Found item: {item['name']}, Price: {item['price']}")
       # item_found = True
        increase = dept["salary"]*1.1
        dept["salary"]=increase
        print(f"The increment:{employees}\n")
      

