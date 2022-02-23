#!/usr/bin/env python
# coding: utf-8

# ### 1. Given two integer numbers, write a Python program to return their product. If the product is greater than 1000, then return their sum. Read inputs from the user.

# In[7]:


num1=int(input("First Number: "))
num2=int(input("Second Number: "))
res= (num1+num2)
product = num1*num2
if product > 1000:
    print("Result ",res) 
else:
    print("Product is not greater than 1000!")


# ### 2. Write a Python program to find the area and perimeter of a circle. Read inputs from the user.

# In[8]:


r=float(input("Radius: "))
area=3.14*r*r
perimeter=2*3.14*r
print(area)
print(perimeter)


# ### 3. Write a Python program to calculate the compound interest based on the given formula. Read inputs
# ### from the user.
# ### A = P * (1 + R/100)
# 
# ### T where P is the principle amount, R is the interest rate and T is time (in years).
# 
# ### Define a function named as compound_interest_<your-student-id> in your program.

# In[12]:


p = float(input("Principal amount: "))
t = float(input("Years: "))
r = float(input("Rate of interest: "))
compound_interest_2018260112 =  p * (pow((1 + r / 100), t)) 
print(compound_interest_2018260112)


# ### 4. Given a positive integer N (read from the user), write a Python program to calculate the value of the
# ### following series.
# 
# ### 1
# ### 2 + 2
# ### 2 + 3
# ### 2 + 4
# ### 2 ..... + N
# ### 2

# In[13]:


def SquareSeries(number):
    if(number == 0):
        return 0
    else:
        return (number * number) + SquareSeries(number-1)
num = int(input("Number: "))
total = SquareSeries(num)
print(total)


# ### 5. Given a positive integer N (read from the user), write a Python program to check if the number is prime or not. Define a function named as prime_find_<your-student-id> in your program.

# In[14]:


def prime_find_2018_2_60_112(n):
 if n>1:
  for i in range(2,n):
   if (n % i) == 0:
    return True
   else:
    False
 else:
  False
x = int(input("Enter any positive integer: ")) 
if (prime_find_2018_2_60_112(x)==True):
 print(x, "is not a prime number") 
else: 
 print("%d is a prime number" %x) 


# ### 6. Given a positive integer n (read from the user), write a Python program to find the n-th Fibonacci number based on the following assumptions. Fn = Fn-1 + Fn-2 where F0 = 0 and F1 = 1

# In[15]:


def fibo(num):
 if num==0:
  return 0
 elif num==1:
  return 1
 else:
  return fibo(num-1)+fibo(num-2)
num = int(input("Enter any positive integer : "))
if(num<0):
 print("Wrong input")
else:
 print(num, "th Fibonacci number is = %d" %fibo(num))


# ### 7. Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of the list. Do not use any built-in function.

# In[17]:


sum = 0
number = [9,7,2,8,0,1,6,4,5,3] 
for i in number: 
 
 sum = i+sum
print("Sum is : ", sum)


# ### 8. Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of the even-indexed elements in the list.

# In[11]:


NumList=[1,2,3,4,5,6]
Sum=0

for j in range (0,len(NumList)):
    if(j % 2 == 0):
        Sum = Sum + NumList[j]
print("\nThe Sum of Even Numbers in this List =  ", Sum)


# ###    9. Given a list of numbers (hardcoded in the program), write a Python program to find the largest and smallest element of the list. Define two functions largest_number<your-student-id> and smallest_number_<your-student-id> in your program. Do not use any built-in function.

# In[6]:


NumList = [10, 300, 20, 40,50, 60,5]




def largest_number_2018260112():
    largest = NumList[0]

    for j in range(1, len(NumList)):


        if (largest < NumList[j]):
            largest = NumList[j]
    print("The Largest Element in this List is : ", largest)




def smallest_number_2018260112():
    smallest = NumList[0]
    for j in range(1, len(NumList)):
        if (smallest > NumList[j]):
            smallest = NumList[j]
    print("The Smallest Element in this List is : ", smallest)

smallest_number_2018260112()
largest_number_2018260112()


# ###### 

# ### 10. Given a list of numbers (hardcoded in the program), write a Python program to find the second largest element of the list.

# In[57]:


def findLargest(arr):

    secondLargest = arr[0]

    largest = arr[0]

    for i in range(len(arr)):

        if arr[i] > largest:
            largest = arr[i]


    for i in range(len(arr)):

        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    return secondLargest


print(findLargest([10, 20, 49,100, 45, 99]))


# In[3]:


N=[100,154,121,135,130,142] 
l=len(N) 
N.sort() 
print("Second largest element is:", N[l-2]) 


# ### 11.Given a string, display only those characters which are present at an even index number. Read inputs from the user.

# In[2]:


string =input("Enter a string: ")
N= len(string)
for j in range(N):
    if(j%2==0):
        print(string[j])


# ### 12. Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string. N must be less than the length of the string. Read inputs from the user. Do not use any built-in function.

# In[11]:


string=input("Enter a string: ")
l=len(string)
n=int(input("Enter a number: "))

new_string=""

for i in range(0,l):
    if i>=n:
        new_string=new_string+string[i]

print("New string is : ",new_string)


# ### 13. Given a string, find the count of the substring “CSE303” appeared in the given string. Do not use any built-in function.

# In[1]:


string = 'This is CSE303 - Statistics for Data Science.Prerequisite of CSE303 is STA102.'
print(string)
sub_string = 'CSE303'
print(sub_string)
count = 0
sub_len=len(sub_string)
for i in range(len(string)):
 if string[i:i+sub_len] == sub_string:
  count += 1
print (count)


# ### 14. Given a string, write a python program to check if it is palindrome or not. Define a function named palindrome_checker_<your-student-id> in your program.

# In[2]:


def palindrome_checker_2018_2_60_112(string):
 string1 = ''.join(reversed(string))
 if(string==string1):
  return True
 else:
    return False
string=input("String: ") 
check = palindrome_checker_2018_2_60_112(string)
if (check): 
 print("Palindrome") 
else: 
 print("Not palindrome") 


# ### 15. Given a two list of numbers (hardcoded in the program), create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list.

# In[3]:


lis1=[11,22,33,44,55,66,77,88,99] 
lis2=[11,21,22,32,33,43,44,54,55,65,66,76,77,87,88,98] 
odd=[] 
even=[] 
l1=len(lis1) 
l2=len(lis2) 
print("List 1 is : ", lis1) 
print("Odd numbers from list 1 : ") 
for i in range (0,l1): 
 if(lis1[i]%2!=0):
  odd.append(lis1[i])
print(odd) 
print("List 2 is : ", lis2) 
print("Even numbers from list 2 : ") 
for i in range (0,l2): 
 if(lis2[i]%2==0):
  even.append(lis2[i])
print(even)


# In[ ]:




