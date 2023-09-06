from random import randint
while True :
    chooseGameMode=input("Hello \nFor play with computer send '1' \nFor play with your friend send '2' \nIf you want to exit: type esc or exit or escape in 'user choose' Instead of rock paper and scissors. \nYour choice:")
    if chooseGameMode=="1":
        
        winPoint=float(input("Send win point to end this game:"))
        userPoint=0.0
        computerPoint=0.0
        while (winPoint*2)>1:
            value=randint(1,3)
            if value==1:
                computerChoose="rock"
            elif value==2:
                computerChoose="paper"
            elif value==3:
                computerChoose="scissors"
            userchoose=input("Rock... \nPaper... \nScissors... \nChoose one:").lower()
            print(f"Computer choose is:{computerChoose}")
            if ( userchoose==computerChoose ):
                print("You got 0.5 point")
                userPoint += 0.5
                computerPoint += 0.5
            elif (userchoose=="rock" and computerChoose=="scissors") or (userchoose=="scissors" and computerChoose=="paper") or (userchoose=="paper" and computerChoose=="rock"):
                print("You got 1 point")
                userPoint += 1.0
            elif (userchoose=="rock" and computerChoose=="paper") or (userchoose=="scissors" and computerChoose=="rock") or (userchoose=="paper" and computerChoose=="scissors"):
                print("You didn't get any point this round")
                computerPoint += 1.0
            elif (userchoose=="esc") or (userchoose=="exit") or (userchoose=="escape"):
                break
            else :
                print("Check your input and try again.")
        
            if (computerPoint>=winPoint) or (userPoint>=winPoint):
                break
            print(f"your point = {userPoint} \ncomputer point = {computerPoint}")
        print(f"---------------------------------- \n \n \nyour point = {userPoint} \ncomputer point = {computerPoint}")
        if userPoint>computerPoint :
            print("You won :)))))")
        elif computerPoint>userPoint :
            print("You lost :((((")
        elif computerPoint==userPoint :
            print("This is draw :////")
        
        break

    elif chooseGameMode=="2":
        
        winPoint=float(input("Send win point to end this game:"))
        player_1_Point=0.0
        player_2_Point=0.0
        while (winPoint*2)>1 :
            player_1=input("Player1 please choose:").lower()
            player_2=input("Player2 please choose:").lower()
            if ( player_1==player_2 ):
                print("Player1 got 0.5 point \nPlayer2 got 0.5 point")
                player_1_Point += 0.5
                player_2_Point += 0.5
            elif (player_1=="rock" and player_2=="scissors") or (player_1=="scissors" and player_2=="paper") or (player_1=="paper" and player_2=="rock"):
                print("Player1 got 1 point \nPlayer2 got 0 point")
                player_1_Point += 1.0
            elif (player_1=="rock" and player_2=="paper") or (player_1=="scissors" and player_2=="rock") or (player_1=="paper" and player_2=="scissors"):
                print("Player1 got 0 point \nPlayer2 got 1 point")
                player_2_Point += 1.0
            elif (player_1=="esc") or (player_1=="exit") or (player_1=="escape") or (player_2=="esc") or (player_2=="exit") or (player_2=="escape"):
                break
            else :
                print("Check your input and try again.")
        
            if (player_1_Point>=winPoint) or (player_2_Point>=winPoint):
                break
            print(f"Player1 points = {player_1_Point} \nPlayer2 points = {player_2_Point}")
        print(f"---------------------------------- \n \n \nPlayer1 points = {player_1_Point} \nPlayer2 points = {player_2_Point}")
        if player_1_Point>player_2_Point:
            print("Player1 won")
        elif player_2_Point>player_1_Point:
            print("Player2 won")
        elif player_1_Point==player_2_Point:
            print("This is a draw :////")
        
        break

    elif (chooseGameMode=="esc") or (chooseGameMode=="exit") or (chooseGameMode=="escape"):
        
        print("Thanks for run this game. Try again later....")
    
        break

    else:
        print("Watch your input!!! \nTry again")
