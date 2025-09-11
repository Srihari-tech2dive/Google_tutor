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