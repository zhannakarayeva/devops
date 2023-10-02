#create a program that calculates the grade letter of student
#Ask user their grade as int num.
#Print `Not a a valid grade if the grade is lower than 0 or bigger than 100
#Print A+ if the grade is higher than 94
#Print A if the grade is in between 85-94 inclusive
#Print B if the grade is in between 75 and 84 inclusive.
#Print C if the grade is in between 65 and 74 inclusive
#Print grade does not meet expectations when the grade is lower than 65

grade=int(input("What is your grade:"))
if 100<grade or grade<0:
  print("Not a a valid grade")
elif grade>94:
  print("A+")
elif   85<=grade<=94:   #85<=grade and grade <= 94
  print("A")
elif   75<=grade<=84:
  print("B")
elif   65<=grade<=74:
  print("C")
elif   grade<65:
  print("does not meet expectations")
