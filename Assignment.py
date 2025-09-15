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