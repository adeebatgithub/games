from os import system
from random import choice
from time import sleep

class tictactoe:

    def __init__(self):
        pass
    
    def display_bord(self,position_dict):

        a = position_dict.get(1," ")
        b = position_dict.get(2," ")
        c = position_dict.get(3," ")
        d = position_dict.get(4," ")
        e = position_dict.get(5," ")
        f = position_dict.get(6," ")
        g = position_dict.get(7," ")
        h = position_dict.get(8," ")
        i = position_dict.get(9," ")

        bord = f''' 

                        |     |
                    {a}   |  {b}  |  {c}
                  ______|_____|_____
                        |     |     
                    {d}   |  {e}  |  {f}
                  ______|_____|_____
                        |     |     
                    {g}   |  {h}  |  {i}
                        |     |

'''
        system("clear")
        print("="*56)
        print(bord)
        print("="*56)

    def check_win(self,d):

        if d[1]!=" " and d[2]!=" " and d[3]!=" ":
            if d[1] == d[2] == d[3]:
                return True
        if d[4]!=" " and d[5]!=" " and d[6]!=" ":
            if d[4] == d[5] == d[6]:
                return True
        if d[7]!=" " and d[8]!=" " and d[9]!=" ":
            if d[7] == d[8] == d[9]:
                return True
        
        if d[1]!=" " and d[4]!=" " and d[7]!=" ":
            if d[1]==d[4]==d[7]:
                return True
        if d[2]!=" " and d[5]!=" " and d[8]!=" ":
            if d[2]==d[5]==d[8]:
                return True
        if d[3]!=" " and d[6]!=" " and d[9]!=" ":
            if d[3]==d[6]==d[9]:
                return True

        if d[1]!=" " and d[5]!=" " and d[9]!=" ":    
            if d[1] == d[5] == d[9]:
                return True
        if d[3]!=" " and d[5]!=" " and d[7]!=" ":
            if d[3] == d[5] == d[7]:
                return True

        lst = [x for x in d if d[x] == " "]
        if len(lst) == 0:
            return "draw"

    def ai_player(self, position_dict):
        
        move_lst = [x for x in position_dict if position_dict[x] == " "] 
        win_move = 0
        for symbol in ["X", "O"]:
            for move in move_lst:
                check_dict = {k:v for k,v in position_dict.items()}
                check_dict[move] = symbol
                is_win = self.check_win(check_dict)
                if is_win == True:
                    win_move = move
                    my_move = win_move
                    break
            if is_win:
                break
                

        if win_move == 0:
            my_move = choice(move_lst)
        return my_move

    def two_player(self):
        
        position_dict = {
                1: " ",2: " ",3: " ",
                4: " ",5: " ",6: " ",
                7: " ",8: " ",9: " ",
            }
        player_1 = "O"
        player_2 = "X"
        self.display_bord(position_dict)
        player = 1
        while 1:
            
            player_inp = int(input(f" player {player}'s turn : "))
            if player == 1:
                position_dict[player_inp] = player_1
                player = 2
            else:
                position_dict[player_inp] = player_2
                player = 1
            
            self.display_bord(position_dict)
            
            status = self.check_win(position_dict)
            if status:
                print(f"player {player} win")
                print()
                break
            if status == "draw":
                print(" Draw ")
                print()
                break
            

    def one_player(self):
        
        position_dict = {                                               1: " ",2: " ",3: " ",
                4: " ",5: " ",6: " ",
                7: " ",8: " ",9: " ",
            }
        player_1 = "O"
        player_2 = "X"
        self.display_bord(position_dict)
        player = "i"
        while 1:

            if player == "i":
                player_inp = int(input(f" your turn : "))
                if position_dict[player_inp] != " ":
                    continue 
                position_dict[player_inp] = player_1
                player = "you"

            else:
                player_inp = self.ai_player(position_dict)
                position_dict[player_inp] = player_2
                player = "i"
                print(" my turn")
                sleep(0.5)

            self.display_bord(position_dict)
            
            status = self.check_win(position_dict)
            if status == True:
                print(f" {player} win")
                print()
                break
            if status == "draw":
                print("Draw")
                print()
                break

if __name__ == "__main__":

    game = tictactoe()
   
    system("clear")
    print("<===== TICTACTOE =====>")
    print("="*56)

    print("[1] single player")
    print("[2] two player")
    print()
    no_player = input("select : ")
    if no_player == "1":
        game.one_player()
    if no_player == "2":
        game.two_player()
