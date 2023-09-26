
#input function allows us to work with dynamic values,because values will be given by user when the code runs
#input function will always give the data as text(string), so we should convert it according what we need using functions like(int(),float(),bool())



#Example of using input function
print('Hello please enter your age')
var1 = input()
print('Your age is '+ var1)         #this will print user's input
print(type(var1))   #Type will be <class 'str'> (text)


#Print true if the user is older than 21, print false otherwise

print('What is your age?')
is_older = (int(var1)>21)
print(is_older)








var2 = int(input("Enter your age: ") )

print ("The user's age is",var2) # This will print user's input.
print (type(var2)) # Type will be <class 'int'> (text)

# Print true if the user is older than 21, print false otherwise.
is_older = var2 > 21

print("Is user bigger than 21? ",is_older)






















