

n= int(input("Input a number"))

# first two terms
n1, n2 = 0, 1
count = 0

if n <= 0:
   print("Invalid number")
elif n == 1:
   
   print(n1)

else:
  
   while count < n:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
