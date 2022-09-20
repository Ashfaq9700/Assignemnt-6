#1. Write a python script to check whether a given number is positive or non-positive
"""Solution
userInput = int(input("Enter Number to Check Positive OR Non-Positive : "))

if(userInput > 0):
    print("Positive")

else:
    print("Non-Positive")
"""

#2. Write a python script to check whether a given number is divisible by 5 or not
"""Solution
userInput = int(input("Enter Number to Check whether a given number is divisible by 5 or not : "))

if(userInput%5 == 0):
    print("Divisible")

else:
    print("Not-Divisible")
"""

#3. Write a python script to check whether a given number is even or odd
"""Solution
userInput = int(input("Enter Number to check whether a given number is even or odd "))

if(userInput%2 == 0):
    print("Even Number")

else:
    print("ODD Number") 
"""

# 4. Write a python script to print greater between two numbers. Print number only once
# even if the numbers are the same.
"""Solution
num_1 = int(input("Enter First Number : "))
num_2 = int(input("Enter Second Number : "))

if(num_1 > num_2):
    print("First Number is Greatest",num_1)

elif(num_1 == num_2):
    print("Both are Equal",num_1)

else:
    print("Second Number is Greatest",num_2)
"""

#5. Write a python script to print two given words in dictionary order
"""Solution
word_1 = input("Enter First Word : ")
word_2 = input("Enter Second Word :")

if(ord(word_1) < (ord(word_2))):
    print(word_1,word_2)

else:
    print(word_2,word_1)
"""

# 6. Write a python script to check whether a given number is a three digit number or not.
"""Solution
userInput = int(input("Enter Number to check whether Three Digit Number or Not : "))

userInput = int(userInput/100)

if((userInput > 0) and (userInput < 9)):
    print("You have Enterd Three Digit Number")

else:
    print("Invalid Number.")
"""

#7. Write a python script to check whether a given number is positive, negative or zero.
"""Solution
userInput = int(input("Enter a Number : "))

if(userInput > 0):
    print("Positive")
elif(userInput == 0):
    print("Zero")
else:
    print("Negative")
"""

#8. Write a python script to check whether a given quadratic equation has two real &
# distinct roots, real & equal roots or imaginary roots
"""Unable to Understand Question"""

#9. Write a python script to check whether a given year is a leap year or not.
"""Solution
leap_Year = int(input("How Many Days in Your Current Year : "))

if(leap_Year == 366):
    print("Your in Leap Year..!")

else:
    print("It's Not a Leap Year.")
"""

#10. Write a python script to print greater among three numbers. Print number only once
# even if the numbers are the same.
"""
a = 50
b = 500
c = 500

if ((a>b) and (a>c)):
    print("A",a)
elif((b>a) and (b>c)):
    print("B",b)
elif ((c>a) and (c>b)):
    print("C",c)
elif ((a==b) and (a==c) and (b==a) and (b==c) and (c==a) and (c==b)):
    print("All are Equal")
elif ((a==b) and (a<c)):
    print("C",c)
elif ((a==c) and (a<b)):
    print("B",b)
elif ((b==a) and (b<c)):
    print("B",c)
elif ((b==c) and (b<a)):
    print("A",a)
elif((a==b) and (c<a)):
    print("A and B are Equal")
elif((a==c) and (b<a)):
    print("A and C are Equal")
elif((b==c) and (a<b)):
    print("B and C are equal")
else:
    print("No Value is Printed")
    
"""

#11. Write a python script to take the month value in numeric format and display the
#number of days in it.
"""Solution
days_31 = [1,3,5,7,8,10,12]
days_30 = [4,6,9,11,]
days_28 = [2]

num_Month = int(input("Enter Month :"))#1
valid_Month = False

for index in range(len(days_31)):
    if(days_31[index] == num_Month):
        valid_Month = True
        print("31 Days")

for index in range(len(days_30)):
    if(days_30[index] == num_Month):
        valid_Month = True
        print("30 Days")    
for index in range(len(days_28)):
    if(days_28[index] == num_Month):
        valid_Month = True
        print("28 Days")
if (valid_Month == False):
    print("Please Enter Months between 1 to 12 only...!")
    """

#12. Write a python script to accept one complex number from the user and display the
# greater number between real part and imaginary part
""""
comp = complex(input("Enter Complex Number :"))

comp_real = int(comp.real)
comp_imrg = int(comp.imag)

if(comp_real > comp_imrg):
    print(comp_real)
else:
    print(comp_imrg)
"""




    
    



    
    
