import random
L=["Rock","Scissor","Paper"]
while True:
    ccount=0
    ucount=0
    uc=int(input(    '''
    1 I want to play game
    2 No not now later|Exit
    '''
    ))
    if uc==1:
        for a in range(1,4):
            userInput=int(input('''
            1 Rock
            2 Scissor
            3 Paper                    
                                '''))
            if userInput==1:
                uchoice="Rock"
            elif userInput==2:
                uchoice="Scissor"
            elif userInput==3:
                uchoice="Paper"
            cchoice=random.choice(L) 
            if cchoice==uchoice:
                print("user choice",uchoice)
                print("computer choice",cchoice)
                print("game draw this level")
                ucount+=1
                ccount+=1
            elif((uchoice=="Rock" and cchoice=="Scissor") or(uchoice=="Scissor" and cchoice=="Paper") or (uchoice=="Paper" and cchoice=="Rock")):
                print("user choice",uchoice)
                print("computer choice",cchoice)
                print("user win this level")   
                ucount+=1
            else:
                print("user choice",uchoice)
                print("computer choice",cchoice)
                print("computer win this level")
                ccount+=1  
            
        if ucount==ccount:
            print("\n")
            print("Final game draw")
            print("user score",ucount)
            print("computer score",ccount)
        elif ucount>ccount:
            print("\n")
            print("user win the game")
            print("user score",ucount)
            print("computer score",ccount)
        else:
            print("\n")   
            print("computer win the game")
            print("computer score",ccount)
            print("user score",ucount)
                
                
                      
    else:
        break




    #OUTPUT:
    """
    1 I want to play game
    2 No not now later|Exit
    1

            1 Rock
            2 Scissor
            3 Paper
                                1
user choice Rock
computer choice Paper
computer win this level

            1 Rock
            2 Scissor
            3 Paper
                                2
user choice Scissor
computer choice Rock
computer win this level

            1 Rock
            2 Scissor
            3 Paper
                                1
user choice Rock
computer choice Scissor
user win this level


computer win the game
computer score 2
user score 1

    1 I want to play game
    2 No not now later|Exit
    1

            1 Rock
            2 Scissor
            3 Paper
                                1
user choice Rock
computer choice Rock
game draw this level

            1 Rock
            2 Scissor
            3 Paper
                                2
user choice Scissor
computer choice Scissor
game draw this level

            1 Rock
            2 Scissor
            3 Paper
                                3
user choice Paper
computer choice Rock
user win this level


user win the game
user score 3
computer score 2

    1 I want to play game
    2 No not now later|Exit

"""