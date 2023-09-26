#We should create a program to calculate if there is still a ticket 
# for the game tonight. We are given two variables: Capacity of the stadium 
#and the amount of tickets sold. 
# Print True if I can still buy a ticket, False otherwise.


print("what is the capacity of the stadium?")
answerCapacity=input()
print("what is the amount of ticket sold?")
ticketSold=input()
youCanStillBuyTicket=answerCapacity>ticketSold
print(youCanStillBuyTicket)


stadium_capacity=int(input("Please enter the stadium capacity:"))
sold_tickets= int(input("Please enter the amount of tickets sold:"))
is_there_space = stadium_capacity > sold_tickets
print("There is space for the game tonight: ",is_there_space)



