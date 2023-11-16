
import random

print('hello my friend!')

player_name = input('whats is your name? ')
print(f"welcome to scissors rock paper {player_name}")

print('here are the rules :\n'
      +'scissors vs rock : rock wins\n'
      +'rock vs paper : paper wins\n'
      +'scissors vs paper : scissors wins')

print('scissors is 1\n'
      +'rock is 2\n'
      +'paper is 3')      
# starting the game

def game_start(): 
    print('starting......')
    
def game():
    gamer_score = 0
    computer_score = 0  
    
    while True:
        game_start()
        gamer = int(input('pls enter a number: '))
        if gamer <1 or gamer >3 :
             print('choose a number between the given Range')
        elif gamer == 1 :
            gamer_choose = 'scissors'
            break
        elif gamer == 2 :
            gamer_choose = 'rock'
            break
        elif gamer == 3 :
            gamer_choose = 'paper'
            break
        else:
            print('invalid input')
    
    print(f'you picked {gamer_choose} ')
    
        
    print('now is the computer turn.....')
    comp = random.randint(1,3)
    
    while comp == gamer :
         comp  = random.randint(1,3)
        
    if comp == 1:
         comp_choose = 'scissors'
    elif comp == 2 :
         comp_choose = 'rock'
    else:
         comp_choose = 'paper'
    print (f'computer picked {comp_choose}')
         
    #winning:
   
      
    while True:
        
        if (gamer == 1 and comp == 3) or (gamer == 2 and comp == 1):
            print (f'{gamer_choose} vs {comp_choose} \n {player_name} wins')
            gamer_score+=1
            print (f'your score is {gamer_score}')
            
        elif gamer == 3 and comp == 2 : 
            print (f'{gamer_choose} vs {comp_choose} \n {player_name} wins')
            gamer_score+=1
            print (f'your score is {gamer_score}')
            
        if (gamer == 3 and comp == 1) or (gamer == 1 and comp == 2):
            print(f'{gamer_choose} vs {comp_choose} \n computer wins')
            computer_score+=1
            print (f'computer score is {computer_score}')
            
        elif gamer == 2 and comp == 3 :
            print (f'{gamer_choose} vs {comp_choose} \n computer wins')
            computer_score+=1
            print (f'computer score is {computer_score}')
            
        elif gamer == comp:
            print("draw!")
        break    
while True:    
    game()
    answer = input('do you want to play again? (Y/N) ')  
    if answer.lower() == 'n' :
        print(f'thank you for visiting {player_name}')
        input()
        break
    
    while True :
        if answer.lower() == 'y' :
            break
        elif answer.lower() != 'n' or answer.lower() != 'y':
            print('enter a valid answer')
            answer = input('do you want to play again? (Y/N) ')
        
        
        
        
    



























    
    

