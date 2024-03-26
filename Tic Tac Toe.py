from IPython.display import clear_output
import time

# Board squares. '*' is a placeholder for index 0.
XO = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# Player Names
players = ['*', ' ', ' ']

# Symbols that belong to each player (in order)
player_symbols = ['*', ' ', ' ']

winner = [' ']

BoardIsFull = False

KeepPlaying = True



# Displays the Tic Tac Toe game
def display_board(XO):
    
    print('\n'*100)
    print(' {} | {} | {} '.format(XO[7], XO[8], XO[9]))
    print('___ ___ ___\n')
    print(' {} | {} | {} '.format(XO[4], XO[5], XO[6]))
    print('___ ___ ___\n')
    print(' {} | {} | {} '.format(XO[1], XO[2], XO[3]))   



# Takes in players' names
def player_names(players):
    players[1] = input("Who's the youngest player? ").capitalize()
    players[2] = input("Who's the oldest player? ").capitalize()
    return players




# Takes in input from each player to assign X and O to index 1 or 2 of a list
def symbol_choice(player_symbols):
    
    while player_symbols[1] not in ['X', 'O']:
    
        player_symbols[1] = input(f'{players[1]}, choose to be X or O: ').capitalize()
        
        if player_symbols[1] not in ['X', 'O']:
            
            print('That was not an X or an O!')
            
            
    if player_symbols[1] == 'X':
        
        player_symbols[2] = 'O'
        
    else:
        
        player_symbols[2] = 'X'
        
    time.sleep(3)    
    print(f'\n{players[2]}, you are ' + player_symbols[2])
    
    return player_symbols



def instructions_player1(first_player_symbol):
    print(f'Use the number pad to place your {first_player_symbol}\n\n7-9 is the top row, 4-6 is the middle row, etc.')
    print()
    time.sleep(3)

def instructions_player2(second_player_symbol):
    print(f'Use the number pad to place your {second_player_symbol}\n\n7-9 is the top row, 4-6 is the middle row, etc.')
    print()
    time.sleep(3)


# Takes in player 1's position choice, checks to make sure there isn't an X or O there, and updates the board squares.

def player_1_move(XO, FirstTurn):
# takes in player move
    print(f"{players[1]}, it's your turn.")
    print()
    
# Only prints instructions if it is the first turn
    if FirstTurn < 2:
        instructions_player1(player_symbols[1])
        FirstTurn += 1
    
    position = input(f'Place your {player_symbols[1]} when you are ready: ')
    square_empty = False
    
    
# checks if position is in range          
    while position not in ['1','2','3','4','5','6','7','8','9'] or not square_empty:
        
        if position not in ['1','2','3','4','5','6','7','8','9']:
            
# simply requests and accepts player position again.
            clear_output()        
            print('Oops! Try again.')
            print()
            time.sleep(2)
            position = input(f'Place your {player_symbols[1]} on the board: ')
        
# checks if the new position is in range.

        if position in ['1','2','3','4','5','6','7','8','9']:
            
# If it is, proceed to check if the space is full. If so, accept new input and start the check over at the first while loop.
           
            while not square_empty:
                
                if XO[int(position)] == ' ':
                    square_empty = True
                else:
                    print('That space is taken. Try again.\n')
                    position = input(f'Place your {player_symbols[1]} on the board: ')
                          
                    
    XO[int(position)] = player_symbols[1]               
    return XO, FirstTurn





def player_2_move(XO, FirstTurn):
# takes in player move
    print(f"{players[2]}, it's your turn.")
    print()
 
# Only prints instructions if it is the first turn
    if FirstTurn < 2:
        instructions_player2(player_symbols[2])
        FirstTurn += 1
        
    print()
    position = input(f'Place your {player_symbols[2]} when you are ready: ')
    square_empty = False  
            
    while position not in ['1',
                           '2','3','4','5','6','7','8','9'] or not square_empty:
        
        if position not in ['1','2','3','4','5','6','7','8','9']:
# Requests and accepts player position again.
            clear_output()        
            print('Oops! Try again.')
            print()
            time.sleep(2)
            position = input(f'Place your {player_symbols[2]} on the board: ')
        
# checks if the new position is in range.
        if position in ['1','2','3','4','5','6','7','8','9']:
# If it is, proceed to check if the space is full. If so, accept new input and start the check overat the first while loop.           
            
            
            while not square_empty:
                
                if XO[int(position)] == ' ':
                    square_empty = True
                else:
                    print('That space is taken. Try again.\n')
                    position = input(f'Place your {player_symbols[2]} on the board: ')
                          
                    
    XO[int(position)] = player_symbols[2]   
    return XO, FirstTurn




# Checks if the game has been won!
def winner_check(XO):
    if XO[1]==XO[2]==XO[3]!=' ' or XO[4]==XO[5]==XO[6]!=' ' or XO[7]==XO[8]==XO[9]!=' ':
        return True
    elif XO[1]==XO[4]==XO[7]!=' ' or XO[2]==XO[5]==XO[8]!=' ' or XO[3]==XO[6]==XO[9]!=' ':
        return True
    elif XO[1]==XO[5]==XO[9]!=' ' or XO[3]==XO[5]==XO[7]!=' ':
        return True
    else: 
        return False
    
    
    
# Displays the winner, if there is one, and returns them 
def game_end(winner, players, player_symbols):
    
    if winner == players[1]:
        
        time.sleep(.5)
        
        print(f'\n\n{players[1]} won!!')
                
        
    elif winner == players[2]:
        
        time.sleep(.5)
        print(f'\n\n{players[2]} won!!')
                
    else:
        
        time.sleep(.5)
        input('Press enter when you are ready to continue: ')
        print()
        
 #  TURN FUNCTION: 
def run_turn(XO, winner, BoardIsFull, FirstTurn):
        
    if player_symbols[1] == 'X':
            
       display_board(XO)
       time.sleep(1)
            
       print()
            
       XO, FirstTurn = player_1_move(XO, FirstTurn)
       time.sleep(0.5)
       print()
       display_board(XO)
       clear_output()
       time.sleep(1)
            
            
       if ' ' not in XO:
          BoardIsFull = True
          return XO, winner, BoardIsFull, FirstTurn
       if winner_check(XO):
              winner = players[1]
              game_end(winner, players, player_symbols)
              return XO, winner, BoardIsFull, FirstTurn
                
       print()
            
       XO, FirstTurn = player_2_move(XO, FirstTurn)
       time.sleep(.5)
       print()
       display_board(XO)
       time.sleep(1)
            
       if ' ' not in XO:
           BoardIsFull = True
           return XO, winner, BoardIsFull, FirstTurn
       if winner_check(XO):
           winner = players[2]
           game_end(winner, players, player_symbols)
           return XO, winner, BoardIsFull, FirstTurn
            
    else: 
            
        display_board(XO)
        time.sleep(0.5)
            
        print()
            
        XO, FirstTurn = player_2_move(XO, FirstTurn)
        time.sleep(0.5)
        print()
        display_board(XO)
        clear_output()
            
        time.sleep(1)
            
            
        if ' ' not in XO:
            BoardIsFull = True
            return XO, winner, BoardIsFull, FirstTurn
        if winner_check(XO):
            winner = players[2]
            game_end(winner, players, player_symbols)
            return XO, winner, BoardIsFull, FirstTurn
                
        print()
            
        XO, FirstTurn = player_1_move(XO, FirstTurn)
        time.sleep(.5)
        print()
        display_board(XO)
        time.sleep(1)
            
            
        if ' ' not in XO:
            BoardIsFull = True
            return XO, winner, BoardIsFull, FirstTurn
        if winner_check(XO):
            winner = players[2]
            game_end(winner, players, player_symbols)
            return XO, winner, BoardIsFull, FirstTurn
    print('\n\n\n\n\n') 
    time.sleep(3)
    return XO, winner, BoardIsFull, FirstTurn



        
 # GAME SETUP: update all lists with correct player name and player symbol.            
display_board(XO)
print('\nWelcome to Tic Tac Toe!')
time.sleep(3)
print('\n')
input('Press Enter when you are ready to begin. ')
time.sleep(0.5)
print()
player_names(players)
print()


        
while KeepPlaying: 
    
    player_symbols = symbol_choice(player_symbols)
    print('\n')
    time.sleep(3)
    
    XO = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    
    winner = [' ']
    
    BoardIsFull = False
   
    # Counter that is 0 at the beginning of the first turn and 2 once both players have gone.
    FirstTurn = 0
              
    
    
    while winner == [' '] and not BoardIsFull:
        
        XO, winner, BoardIsFull, FirstTurn = run_turn(XO, winner, BoardIsFull, FirstTurn)
        
        if BoardIsFull:
            clear_output()
            print("\n\n\nCat's Game!")
            time.sleep(2)

       
    if input('Do you want to play again? (Enter Y or N): ') == 'n' or 'N':
        KeepPlaying = False
    
    
        



    
    
    
        




































