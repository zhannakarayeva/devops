#Multiple Reassignment
a=b=c=d=5
#These variables are not dependent on each others
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)

a,b,c,d=4,3,2,1       #Numbers can be reassigned
print("After reassignment")
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)

#Python is always look for the last asignment to the line it executing.From top to bottom, from left to right.