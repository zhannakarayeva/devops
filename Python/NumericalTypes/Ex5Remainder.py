
# Suppose you have a box containing 28 colored 
# pencils,  and you want to divide them evenly 
# among 5 friends so that each friend gets 
# the same number of pencils.
#Find out how many pencils each friend will get and find out how many pencils will be left to you.


pencils=28
friends=5
leftToMe=pencils%friends
eachFriendHas=pencils//friends
print(leftToMe)
print(eachFriendHas)