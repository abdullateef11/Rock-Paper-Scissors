import random

#RPS is a game in which rock(R) beats scissors(S), scissors beat paper (P), and paper beats rock

player =""
choices = ['R','P','S']
random_answer= random.choice(choices)
def repeat():
        global player
        player=input('''Pick R for Rock, P for Paper or S for Scissors. :''' )
repeat()

while(player  not in choices):
    print("Invalid input\n")
  
    repeat()
else:
    while(player ==  random_answer):#for a tie
        print("Player  ({}) : Computer ({})".format(player ,random_answer))
        print("It's a tie ")
        repeat()

    else:
         if(player  =="R" and random_answer=="S"):
             print("Player  ({}) : Computer ({})".format(player ,random_answer))
             print("Player wins")
         elif(player  =="S" and random_answer=="R"):
             print("Player  ({}) : Computer ({})".format(player ,random_answer))
             print("Computer wins")
         elif(player  =="S" and random_answer=="P"):
             print("Player  ({}) : Computer ({})".format(player,random_answer))
             print("Player wins")
         elif(player  =="P" and random_answer=="S"):
             print("Player  ({}) : Computer ({})".format(player ,random_answer))
             print("Computer wins")
         elif(player  =="P" and random_answer=="R"):
             print("Player  ({}) : Computer ({})".format(player ,random_answer))
             print("Player wins")
         elif(player  =="R" and random_answer=="P"):
             print("Player  ({}) : Computer ({})".format(player ,random_answer))
             print("Computer wins")



    

