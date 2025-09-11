print("Hello, Placement Drive!")

#nxt
age = 21
name = "Arjun"
print(type(age))   # This will output: <class 'int'>
print(type(name))  # This will output: <class 'str'>

age = 21
name = "Arjun"
print(age)   # This will output: <class 'int'>
print(name)  # This will output: <class 'str'>

#nxt
#Mini-Assignment 1: Getting to Know You
name=input("Enter u r name:")
year=int(input("Enter year u r born:"))
com= input("Target company:")
year1=2025
current_age=year1-year
print(current_age)
print("Hello",name,"!. You are approximately",current_age,"years old.We will work hard to get you into",com)

#nxt
#Mini-Assignment 2: The Number Analyzer
number= int(input("Enter no. :"))
if number==0:
  print("zero")
elif number>0:
  print("positive")
else:
  print("negative")
if number%2==0:
  print("Even")
else:
  print("odd")
