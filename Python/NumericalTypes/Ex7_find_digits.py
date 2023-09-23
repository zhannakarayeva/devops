#four_digit_num = 9876
#Create a program that will find each digit just using
# the variable name. 
# One fact is that number is always going to be 4 digit.

# Note! Every time finding a remainder with 10 gives us 
# last digit from the number. 
#Note! Every time a number is divided by 10 will 
# lose its last digit. 

number=1234
devition=10
result=number//devition    #devide by ten  123
a=number%result            #
print(a)
result2=result//devition   #devide by ten  12
b=result%result2
print(b)
result3=result2//devition  #devide by ten  1
c=result2%devition
print(c)
print(result3)             #the result of what left of all devition



#another example
# four_digit_num = 8765

# last_digit = four_digit_num % 10
# print(last_digit)
# I want to remove the last digit
# three_digit_version = four_digit_num //10

# third_digit = three_digit_version % 10 
# print(third_digit)
# two_digit_version = three_digit_version // 10

# second_digit = two_digit_version % 10
# print(second_digit)

# first_digit = two_digit_version // 10
# print(first_digit)

