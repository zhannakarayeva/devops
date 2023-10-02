# In the factory we need to create a program that can 
# find if we can do the shipment and, if we can do the shipment
# it will tell us how many small package we should ship.
# First we need to get total kilogram of the shipment,
# to reach this total kilogram of shipment we can use small and big packages. 
# Every big package is 5 kilogram and every small packages is 1 kilogram.
# We have limited amount of small and big packages. 
# Ask user how many big and how many small package  they have.
# Ask user what is the total goal kilogram of the shipment.
# Print whether they can ship, if they can ship print how many small packages they need. 
# Assume big packages is used before small packages. 

total_goal_of_the_shipment=int(input("Enter amount of shipment in kg:"))
#In order to reach the number above I need to combine number of small package of big package.
small_packages=int(input("How many small packages in inventory:"))
bit_packages=int(input("How many big packages in inventory:"))
#Small packages weighs in kg, a big package weight 5kg
ideal_needed_big_packages= total_goal_of_the_shipment//5
if bit_packages >= ideal_needed_big_packages:
    ideal_needed_small_packages=total_goal_of_the_shipment%5
    if small_packages>=ideal_needed_small_packages:
        print("We can ship and i need to use ",ideal_needed_small_packages,"amount")
    else:
        print("We cant do shipment because we dont have enough small packages")
elif bit_packages<ideal_needed_big_packages:
    #use all the big packages
    total_amount_from_big_pack=bit_packages*5
    small_pack_needed=total_goal_of_the_shipment-total_amount_from_big_pack
    if small_pack_needed<=small_packages:
        print("I can do the shipment:")
    else:
        print("I cannot do the shipment:")