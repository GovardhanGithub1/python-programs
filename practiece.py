#Using two while loops 
"""
i=1
while i<=5 :
    print("Hello")
    j=1
    while j<=4 :
        print('Hi ')
        j+=1
    i+=1
print('Bye')
"""
#Printing even/odd numbers in a series using while loop
"""
i=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
x=0
while x<len(i) :
    if i[x]%2==0 :
        print(i[x])
    x+=1
"""
#Printing every charactor in a string using while loop
"""
x='LandMark Group'
i=0
while i<len(x) :
    print(x[i])
    i+=1
"""
#Printing even/odd numbers in a series by using for loop
"""
i=[1,2,3,4,5,6,7,8,9,10]
for x in i :
    if x % 2 == 0 :
        print(x)
"""
#Printing every charector in a string by using for loop
"""
x= 'landmark group'
for i in x :
    print(i)
"""
#printing seriece of numbers by using for loop
"""
for i in range(1,21,1) :
    print(i)
"""
#Printing perfect square numbers in between 1 to 500 by using for loop
"""
import math
for i in range(1,500) :
    a = math.sqrt(i)
    if i % a == 0:
        print(i, end=" ")
"""
#Printing candies as per our requirement
"""
x=int(input("How many candies you want?"))
i=1
av = 8
if av<x :
    print("We have ", av, "candies only would you like to continue if yes press Y if no press N")
    j=input()
    if j=='Y' :
        while i<=x :
            if av < i :
                print("Out of stock")
                break
            print('candy', end=" ")
            i+=1
    else :
        print("Thank you")
else :
    while i<=x :
        print('candy', end=" ")
        i+=1
print('\n bye')
"""
#Printing numbers as per our requirements by using break, continue, pass
"""
for i in range(1, 101) :
    if i%3==0 or i%5==0 :
        continue
    print(i)
print("Bye")
"""
#Printing even/odd numbers by using pass
"""
for i in range(1, 101) :
    if i % 2 != 0 :
        pass
    else :
        print(i)
print("Bye")
"""
#Pattern1
"""
for i in range(5):
    print("# "*i)
"""
#Pattern2
"""
for i in range (4) :
    for i in range (4) :
        print("# ", end="")
    print()
"""
#Pattern3
"""
for i in range(4) :
    for i in range(i+1) :
        print("#", end=" ")
    print()
"""
#Pattern4
#x= len(range(4))
#print(x)
"""
for i in range(4) :
    for i in range(4-i) :
        print("#", end=" ")
    print()
"""
#Pattern5
"""
for i in range(4) :
    for j in range(4-i) :
        i+=1
        print(i, end=" ")
    print()
"""
#Pattern6 Not complete yet
"""
for i in ['a','b','c','d'] :
    print(i, end=" ")
    for j in ['p','q','r'] :
        print(j, end=" ")
    print()
"""
#Prime or not
"""
num = 45
for i in range(2,num) :
    if num%i==0 :
        print(num," is not a prime number")
        break
else :
    print(num, " is a prime number")
print("Bye")
"""
#Factorial number
""" 
x=int(input("Factorial of a number"))
j=1
for i in range(1,x+1)  :
    j*=j
print(j)
"""
#Create an array from user inputs
"""
from array import *
arr = array('i',[])
x=int(input("Hey man how many numbers you are going to enter"))
for i in range(x) :
    y = int(input("Enter next value"))
    arr.append(y)
print(arr)
l=int(input("searching value"))
k=0
for j in arr :
    if j==l :
        break
    k+=1
print(k)
print(arr.index(l))
"""
#Adding two arrays by using for loop
"""
from array import *
x=array('i',[1,2,3,4,5])
y=array('i',[6,7,8,9,10])
z=array('i',[])
for i in range(len(x)) :
    z.append(x[i]+y[i])
print(z)
"""
#Finding max,min,sum and sorted values with and without inbuilt functions
"""
from array import *
x=array('i',[32,72,34,56,0]) 
mxv=0
mnv=0
for i in x :
    if i>mxv :
        mxv=i
    elif i<mnv :
        mnv=i
print("Max of num without func ", mxv)
print("Min of num without func ", mnv)
print("Max num of array ",max(x))
print("Min num of array ",min(x))
print("Sum of ayyay ", sum(x))
print(sorted(x))
"""
#Creating Add and Sub function
"""
def add_sub(x,y):
    c=x+y
    d=x-y
    return c, d
result1, result2 = add_sub (10, 4)
print(result1, result2)
def greet():
    print("Hello")
    print("Good Morning")
greet()
"""
#Printing Fibonacci series
"""
x=[]
def feb(n) :
    a=0
    b=1
    x.append(a)
    x.append(b)
    if n==1 :
        print(a)
    elif n<0 :
        print("It's accept only positive numbers")
    else:
        for i in range(2,n) :
            c=a+b
            a=b
            b=c
            x.insert(i,c)
            if c>n :
                print(a)
                break
        print(x)
feb(100)
"""
#Changing recursion limits
"""
from sys import *
x=getrecursionlimit()
print(x)
setrecursionlimit(20)
print(getrecursionlimit())
"""
#Printing factorial of given number by using recursion
"""
def fact(n) :
    if n==0 :
        return 1
    return n*fact(n-1)
x=fact(5)
print(x)
"""
#Ananymos function
"""
def square(a) :
    return a*a
result = square(4)
print(result)
f=lambda a : a*a
print(f(4))
"""
#Filter, map, reduce in lamda
"""
from functools import *
x=[1,21,3,34,5,32,11,24]
print(list(filter(lambda a : a%2==0,x)))
print(list(map(lambda a : a*2, list(filter(lambda a : a%2==0,x)))))
print(reduce(lambda a, b: a+b, list(map(lambda a : a*2, list(filter(lambda a : a%2==0,x))))))
"""
"""
from functools import *
x=[1,2,13,4,5,7,8]
evens=list(filter(lambda a : a%2==0, x))
print(evens)
doubles = list(map(lambda a : a*2, evens))
print(doubles)
sum = reduce(lambda a, b : a+b, doubles)
print(sum)
"""
#OOPs concepts
"""
class car:
    def feature1(f,name,color):
        f.name=name
        f.color=color
        print('from feture1',f.name, f.color)

c1=car()
c1.feature1('bmw','red')
"""
#Oracle DB connection
"""
import cx_Oracle
constr='OT_SRC_DEV/admin@localhost:1521/xe'
conn = None
try :
    conn = cx_Oracle.connect(constr)
    cur = conn.cursor()
    cur.execute('select * from agents')
    for i in cur :
        print(i)
except Exception as err :
    print('Error, while connecting to the DB')
    print(err)
finally :
    cur.close()
    conn.close()
"""
#Zip two things
"""
names = ('john','deo','lusy')
laps = ('hp', 'mac', 'lenovo')
full = list(zip(names, laps))
print(full)
"""
# Calculator
"""
sum=0
b=1
while b>=1 :
    a=int(input("Enter a number"))
    sum=sum+a
    symbol=input('')
    if symbol == '=' :
        break
    b+=1
print(sum)
"""
"""
import cx_Oracle
mydb = cx_Oracle.connect('hr/hr@localhost:1521/xe')
cur=mydb.cursor()
cur.execute('select * from emp')
for i in cur :
    print(i)
cur.close()
mydb.close()
"""
print("welcome to python calculator")
print("You can enter any kind of equation and press enter")
a = eval(input(''))
print('This is your total : ',a)