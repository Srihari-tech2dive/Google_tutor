#1q workout The Pyramid Builder 
number=int(input("Enter the no. :"))
for i in range(number):
  for j in range(i+1):
    print("*",end="")
  print()

#2q workout The Prime Number Checker 
number=int(input("Enter the no. :"))

is_prime = True
if number <= 1:
  is_prime = False

else:
  for i in range(2, number):
    if number % i == 0:
      is_prime = False  
      break

if is_prime:
  print(f"{number} is a prime number.")
else:
  print(f"{number} is not a prime number.")

#3q Sum of All Numbers

li=[1,5,2,9,4]
total=0
for i in li:
  total+=i
print(total)

#4q Countdown

n=10
while n>0:
    print(n)
    n-=1
print("Liftoff!")

#5q Print Even Numbers
for i in range(1,21):
  if i%2==0:
    print(i)

#6q Find the Maximum Number
max_num = [45, 67, 23, 89, 12, 55]
max_element = max_num[0] #

for num in max_num:
    if num > max_element:
        max_element = num

print(max_element)

#7q FizzBuzz Challenge 
for i in range(1,101):
  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif i%3==0:
    print("Fizz") 
  elif i%5==0:
    print("Buzz")
  else:
    print(i)

#8q Count the Vowels

def count_vowels(input_string):

  vowel_count = 0

  vowels = "aeiou"
  
  for char in input_string.lower():

    if char in vowels:

      vowel_count += 1
      
  return vowel_count


my_string = "Hello World"
result = count_vowels(my_string)
print(f"The number of vowels in '{my_string}' is: {result}")

#9q Prime Number Checker

def is_prime(n): 

  if n <= 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True
num_to_check = int(input("Enter a no. :"))
if is_prime(num_to_check):
  print(f"{num_to_check} is a prime number.")
else:
  print(f"{num_to_check} is not a prime number.")


#10q Print a Triangle Pattern

for i in range(6):
  for j in range(i):
    print("*",end=(""))
  print()

# #11q Simple Password Guessing Game

# secret_pass= "1234"

# attempts=3

# while True:
#   print("Guess the secret password")
#   password=input("Enter 4-digit password:")
#   for i in password :
#     if i in secret_pass:
#       attempts-=1
#       print(i)
#       print(f"The number attempts remaining is",attempts) 

#   if attempts==0:
#         print("Try next time")
      
#   else:
#         print("Correct password")
#         break
   
secret_pass = "1234"
attempts_left = 3

while attempts_left > 0:
  guess = input(f"Guess the 4-digit password [{attempts_left} attempts left]: ")

  if guess == secret_pass:
    print("Correct password! You win!")
    break 
  else:
    print("Wrong password.")
    attempts_left -= 1 


if attempts_left == 0:
  print("You are out of attempts. Try next time.")