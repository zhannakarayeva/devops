
#  Leap Year
# A year is leap if it is divisible by 4 but not by 100 
# unless it is also divisible by 400. 
# Write a program that takes a year as input 
# and prints True if it's a leap year, False otherwise.
#2000, 2024,2020,1916

year=int(input("What is the year?"))
result=(year%4 or year%400 )and  year%100 !=0
print(result)

#NOTE: if the number x is divisible by number z it means   x%z==0 -->True















