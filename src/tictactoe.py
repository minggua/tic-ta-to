import tkinter
from turtle import window_height

def set_tile(row, col):
    global curr_player

    if (game_over):
        return

    if board[row][col]["text"] != "":
        #already taken spot
        return

    board[row][col]["text"] = curr_player #mark the board
    
    if curr_player == playerX:#switch player 
        curr_player = playerO 
    else:
        curr_player = playerX

    label["text"] = curr_player+"'s turn"

    #check winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    #horizontal, check 3 rows
    for row in range(3):
        if(board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=color_blue)
            for col in range(3):
                board[row][col].config(foreground=color_blue, background=color_red)
            game_over = True
            return
        
    #vertical, check 3 columns
    for col in range(3):
        if(board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"]
           and board[0][col]["text"] != ""):
            label.config(text=board[0][col]["text"]+" is the winner!", foreground=color_blue)
            for row in range(3):
                  board[row][col].config(foreground=color_blue, background=color_red)
            game_over = True
            return
        
    #diagnolly
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_blue)
        for i in range(3):
            board[i][i].config(foreground=color_blue, background=color_red)
        game_over = True
        return

    #anti-diagonally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " is the winner!", foreground=color_blue)
        board[0][2].config(foreground=color_blue, background=color_red)  
        board[1][1].config(foreground=color_blue, background=color_red)  
        board[2][0].config(foreground=color_blue, background=color_red)   
        game_over = True
        return
    
    #tie
    if (turns == 9):
        label.config(text="It's a tie!", foreground=color_blue)
        game_over = True

def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label["text"] = curr_player + "'s turn"

    for row in range(3):
        for col in range(3):
            board[row][col].config(text="", foreground="white", background=color_dark_grey)

#game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#3b83bd"
color_red = "#e74c3c"
color_dark_grey = "#2c3e50"

turns = 0
game_over = False

#window setup
window = tkinter.Tk()  # create the game window
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player + "'s turn", font=("Consolas", 20), background=color_dark_grey,
                       foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for col in range(3):
        board[row][col] = tkinter.Button(frame, text="", font=("Consolas", 40, "bold"),
                                         background=color_dark_grey, foreground="white", width=5, height=1,
                                         command=lambda row=row, col=col: set_tile(row, col))
        board[row][col].grid(row=row + 1, column=col)

button = tkinter.Button(frame,text="restart", font=("Consolas", 20), background=color_dark_grey,
                         foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

#center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2)-(window_width/2))
window_y = int((screen_height/2)-(window_height/2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


window.mainloop()
