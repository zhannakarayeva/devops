#There is 20  dovops in the comp that should be equaly assigned to each of 8 scrum teams.
#Find out how many dev ops engineer will not be assigned with the team
#Also find out how many devops engineers will be in each scrum team


devops=20
scrums=8
resultLeft=devops%scrums
totalInScrumTeam=devops//scrums
print(resultLeft)
print(totalInScrumTeam)



num_deveops, num_scrums =20,8
print("Each team will have",num_deveops//num_scrums,"devops engineers")
print("After the assignment there will be ",num_deveops%num_scrums," will be annasigned")


# % reminder will be the left over after the divition.
# // double slash is actially show the result without 