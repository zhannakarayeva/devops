
# Logical Operators in Python

## AND operator
- `and` operator checks if **all** conditions are True. For ex:
```py
#Lets write a program to see if a person can drive:
# In order to drive they must be over 15 years old and they must have a valid license
age = 18
has_license = True
can_drive = has_lisense and age > 16
```
print=int(input("What is your age?"))

## OR operator
- `or` operatr checks if at least one condition is True. For ex:
```py
#A worker can get rest when it is weekend or when it is holiday.
is_holiday = True
is_weekend = False
can_rest = is_holiday or is_weekend
```

## NOT operator
- Reverses the result of a boolean variable. For ex:
```py
b1=True
b1=not b1
print (b1)  #False
b1 = not b1
print(b1)  #True
```

```py
print(True and not False) #True
print(not True and True)  #False
print(True and True and True and False) #False
print(not False or False)  #False
print(False and False) #False
print(False or False) #False

#Using both `and`   and   `or` operators at the same time
#In python `and` operator will be executed before the `or` operator
print(False or True and False)  #False
#NOTE: not operator will be executed the `and` and `or` operators



 










```




















