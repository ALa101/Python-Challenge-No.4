"""
            3.wants to invite
 Ask how many people the user wants to invite to a party.
 If they enter a number below10,
 ask for the names and after each name display “[name] has been invited”.
 If they enter a number which is 10 or higher,
 display the message “Too many people”.
 Upload program to GitHub and write the link?
"""
people = []
many = int(input("how many people the user wants to invite to a party ?\n\r"))
if many.__lt__(10):
    for i in range(many):
        people.append(input(str(i+1) +"-Enter the name of the (" +str(i+1) +") invitee :"))
        print(people[i] + " :has been invited")
else:
    print("Too many people\n\t\tSory Dear  ^_^")
