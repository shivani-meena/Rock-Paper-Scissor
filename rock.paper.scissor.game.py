import random
# print("Winning Rules of the Rock paper scissor game as follows: \n"+"Rock vs paper->paper wins \n"
# + "Rock vs scissor->Rock wins \n"+"paper vs scissor->scissor wins \n")
l=["rock","scissor","papper"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''game start: 1:yes 
            2:no'''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input("enter,1(rock),2(scissor),3(papper)"))
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="scissor"
            elif userinput==3:
                uchoice="papper"
            cchoice=random.choice(l)
            if cchoice==uchoice:
                print("computer value",cchoice)
                print("user value",uchoice)
                print("game draw")
                ucount=ucount+1
                ccount=ccount+1
            elif(uchoice=="rock" and cchoice=="scissor")or (uchoice=="papper" and cchoice=="rock")or (uchoice=="scissor"and cchoice=="papper"):
                print("computer value",cchoice)
                print("user value",uchoice)
                print("you win")
                ucount=ucount+1
            else:
                print("computer value",cchoice)
                print("user value",uchoice)
                print("computer win")
                ucount=ucount+1
                ccount=ccount+1
            if ucount==ccount:
                print("final game draw....")
                print("user score",ucount)
                print("computer score",ccount)
            elif ucount>ccount:
                print("final you draw....")
                print("user score",ucount)
                print("computer score",ccount)
            else:
                print("computer win the game....")
                print("user score",ucount)
                print("computer score",ccount)
    else:
        break
