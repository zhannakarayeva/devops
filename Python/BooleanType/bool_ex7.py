# John wants lose 10 pounds in one month. 
# There are multiple conditions to lose 10 pounds in a month 
# John needs to walk 10000 steps daily  OR needs to run at least
# 4 miles a day.  and Addition to these , John needs to eat less 
# than 1500 calories daily. We should create a program to calculate 
# if John can loose weight or not 
# daily steps,running distance and daily calory intake will be given by users.
#Our goal is to print True when John can loose weight and print False otherwise.

steps=int(input("How many steps do you walk dayly?"))
milesRun=int(input("How many miles do you run daily?"))
calories=int(input("How many calories do you eat daily?"))
goal=steps>=1000 or milesRun>=10 and calories<=1500
print(goal)












