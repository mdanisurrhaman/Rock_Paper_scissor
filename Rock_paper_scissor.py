import random

list1=["rock","scissor","paper"]

"""
rock vs paper->paper wins
rock vs scissor-> rock wins
paper vs scissor->scissor wins

"""

while True:
    ccount=0
    ucount=0

    uc=int(input('''

Game start........
1 yes
2 No| Exit


            '''))
    

    if uc== 1:
        
        
        for a in range(1,6):
            
            userInput=int(input('''


1 Rock
2 Scissor
3 Paper
                   '''))
            
            if userInput==1:
                uchoice="rock"
                         
            elif userInput==2:
                 uchoice="Scissor"

            elif userInput==3:
                 uchoice="paper"
                 
            
                 cchoice= random. choice(list1)

            if cchoice==uchoice:
                     print('computer value',cchoice)
                     print('user value',uchoice)
                     print('game draw')

                     ucount=ucount+1
                     ccount=ccount+1

            elif(uchoice=="rock" and cchoice=="scissor")or (uchoice
                    =="paper" and cchoice=="rock") or (uchoice=="scissor" and cchoice=="paper"):
                     print('computer value',cchoice)
                     print('user value',uchoice)
                     print('you win')
                     ucount=ucount+1

            else:
                     print('computer value',cchoice)
                     print('user value',uchoice)
                     print('computer win')
                     ccount=ccount+1



            if ucount==ccount:
                print("Final Game draw......")
                print("User Score",ucount)
                print("Computer score",ccount)

            elif ucount>ccount:
                 print("Final you win the game......")
                 print("User Score",ucount)
                 print("Computer score",ccount)
                
        else:
              print("Final computer win the game......")
              print("User Score",ucount)
              print("Computer score",ccount)
              
               
               
                    
                     
                     
                 
                

                 


    else:
            
            break














    
