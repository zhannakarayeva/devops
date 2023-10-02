#Ask user to enter 2 equal int variables. And if user inters two numbers that are same we will print 'You entered two equal numbers'
#if user entered two different numbers we will print 'You didnt follow the instruction'.

num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
if num1==num2:
  print("You entered two equal numbers")
if num1!=num2:
    print("You didnt follow the instruction")

#Note! By using elif statement we are telling python that both conditions cant't be True


