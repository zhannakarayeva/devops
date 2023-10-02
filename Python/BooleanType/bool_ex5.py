# Company wants to increase their server according to their CPU usage. 
# Create a python program that gets average cpu usage as an input 
# and prints True if we need to launch more servers for our application.
# When average cpu usage is between 40 and 70 inclusive
# we should launch a new server.

print("what is avarage CPU usage? ")
CPU_usage=int(input())
needToLounch=CPU_usage>=40 & CPU_usage>=70
print(needToLounch)






attendance=int(input("What is your attendance?"))
grade=int(input("what is your grade?"))
pass_or_not=grade>80 & attendance>90
print(pass_or_not)


