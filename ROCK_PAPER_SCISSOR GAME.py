#Rock Paper Scissors
import random


print("""
         ************************************************************
         *                                                          *
         *        Welcome to the Rock, Paper, Scissors Game!        *
         *                                                          *
         ************************************************************

         """)

print('\n a.Two player game \n b. Playe with computer \n')
Option=input('Select your choice')

if(Option=='a'):
 print("\n Select your choice ")
 print("\n 1.Rock \n 2.Paper \n 3.Scissors \n")

 m=int(input('Enter Number of Matches'))
 score_p1=0
 score_p2=0


 for i in range(0,m):
    
  a=int(input("Player1 select your choice"))
  b=int(input("Player2 select your choice"))

  if(a==1):
    if(b==2):
        print('Player2 is Winner')
        score_p2=score_p2+1
    elif(b==3):
        print('Player1 is Winner')
        score_p1=score_p1+1
    elif(b==1):
        print('Match is tie')
    else:
        print('error')
  elif(a==2):
    if(b==1):
        print('Player1 is Winner')
        score_p1=score_p1+1
    elif(b==2):
        print('Match is Tie')
    elif(b==3):
        print('Player2 is Winner')
        score_p2=score_p2+1
    else:
        print('error')
  elif(a==3):
    if (b==1):
        print('Player2 is Winner')
        score_p2=score_p2+1
    elif(b==2):
        print('Player1 is Winner')
        score_p1=score_p1+1
    elif(b==3):
        print('Match is Tie')
    else:
        print('error')
  else:
    print('error')
  print('\n')
    
 print('Score of Player1 is =',score_p1)
 print('Score of Player2 is =',score_p2)

 if(score_p1>score_p2):
    print("""
                 ******************************
                 *                            *
                 *     PLAYER1 IS WINNER      *
                 *                            *
                 ******************************""")
 elif(score_p1<score_p2):
    print("""    ******************************
                 *                            *
                 *     PLAYER2 IS WINNER      *
                 *                            *
                 ******************************""")
 else:
    print("""     **************
                  *            *
                  *     TIE    * 
                  *            * 
                  ************** """)

elif(Option=='b'):
    print("\n Select your choice ")
    print("\n 1.Rock \n 2.Paper \n 3.Scissors \n")

    m=int(input('Enter Number of Matches'))
    score_p1=0
    score_p2=0


    for i in range(0,m):
    
      a=int(input("Player1 select your choice"))
      b=[1,2,3]
      computer=random.choice(b)
      print('Computer select',computer)

      if(a==1):
          if(computer==1):
              print('Match is Tie')
          elif(computer==2):
              print('Computer is Winner')
              score_p2=score_p2+1
          elif(computer==3):
              print('player1 is winner')
              score_p1=score_p1+1
          else:
              print('error')
      elif(a==2):
          if(computer==1):
              print('Player1 is Winner')
              score_p1=score_p1+1
          elif(computer==2):
              print("Match is Tie")
          elif(computer==3):
              print("Computer is Winner")
              score_p2=score_p2+1
          else:
              print('Error')
      elif(a==3):
          if(computer==1):
              print('Computer is Winner')
              score_p2=score_p2+1
          elif(computer==2):
              print('Player1 is Winner')
              score_p1=score_p1+1
          elif(computer==3):
              print('Match is Tie')
          else:
              print('Error')
      else:
          print('you select wrong choice')
      print('\n')
    print('\n Score of Player1 is = ',score_p1)
    print('\n Score of Computer is =',score_p2)
    if(score_p1>score_p2):
        print("""
                 ******************************
                 *                            *
                 *     PLAYER1 IS WINNER      *
                 *                            *
                 ******************************
                                                """)
    elif(score_p1<score_p2):
        print("""
                 ******************************
                 *                            *
                 *     COMPUTER IS WINNER     *
                 *                            *
                 ****************************** """)
    else:
        print("""
                  **************
                  *            *
                  *     TIE    * 
                  *            * 
                  **************""")
