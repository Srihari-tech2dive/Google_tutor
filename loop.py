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