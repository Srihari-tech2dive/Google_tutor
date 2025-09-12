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


# try
# tasks = [ ]
# menu_list=["add","view","remove","exit"]
# while True :
#   menu =input("Enter any one: add,\nview,\nremove,\nexit:\n").lower()
#   for i in menu:
#     if menu=="add":
#       new=input("Enter new task:")
#       tasks.append(new)
#     elif menu=="view":
#       for t in tasks:
#         if tasks==0:
#           print("Your to-do list is empty")
#         else:

#           print(t)
#     elif menu=="remove":
#       print("The tasks are",tasks)
#       delete=int(input("The task you want to remove(say the position of it):"))
#       if delete<0 or delete>=len(tasks):
#         print("Invalid position")
#       else:
#         tasks.remove(delete)
#     elif menu=="exit":
#       break
#     else:
#       print("Invalid input")


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