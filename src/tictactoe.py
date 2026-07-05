import tkinter
from turtle import window_height

def set_tile(row, col):
    global curr_player

    if (game_over):
        return

    if board[row][col]["text"] != "":
        return

    board[row][col]["text"] = curr_player

    if curr_player == playerX:
        curr_player = playerO
        label["text"] = player2_name + "'s turn(o)"
    else:
        curr_player = playerX
        label["text"] = player1_name + "'s turn(x)"

    check_winner()


def flash_line(line, count=0):
    if count >= 6:
        for (r, c) in line:
            board[r][c].config(background=color_red)
        return
    color = color_red if count % 2 == 0 else color_dark_grey
    for (r, c) in line:
        board[r][c].config(background=color)
    window.after(150, lambda: flash_line(line, count + 1))


def on_enter(e, button):
    if button["text"] == "" and not game_over:
        button.config(background=color_blue)


def on_leave(e, button):
    if button["text"] == "" and not game_over:
        button.config(background=color_dark_grey)


def check_winner():
    global turns, game_over, player1_score, player2_score
    turns += 1

    lines = []
    for i in range(3):
        lines.append([(i, 0), (i, 1), (i, 2)])
        lines.append([(0, i), (1, i), (2, i)])
    lines.append([(0, 0), (1, 1), (2, 2)])
    lines.append([(0, 2), (1, 1), (2, 0)])

    for line in lines:
        pos1, pos2, pos3 = line
        val1 = board[pos1[0]][pos1[1]]["text"]
        val2 = board[pos2[0]][pos2[1]]["text"]
        val3 = board[pos3[0]][pos3[1]]["text"]

        if val1 == val2 == val3 != "":
            winner_name = player1_name if val1 == playerX else player2_name

            if val1 == playerX:
                player1_score += 1
            else:
                player2_score += 1
            score_label.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")

            label.config(text=winner_name + " wins!", foreground=color_blue)
            for (r, c) in line:
                board[r][c].config(foreground=color_blue)
            flash_line(line)
            game_over = True
            return

    if turns == 9:
        label.config(text="It's a tie!", foreground=color_blue)
        game_over = True

    #horizontal, check 3 rows
    for row in range(3):
        if(board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            winner_name = player1_name if board[row][0]["text"] == playerX else player2_name

            if board[row][0]["text"] == playerX:
                player1_score += 1
            else:
                player2_score += 1
            score_label.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")

            label.config(text=winner_name + " wins!", foreground=color_blue)
            for col in range(3):
                board[row][col].config(foreground=color_blue, background=color_red)
            game_over = True
            return

    #vertical, check 3 columns
    for col in range(3):
        if(board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"]
           and board[0][col]["text"] != ""):
            winner_name = player1_name if board[0][col]["text"] == playerX else player2_name

            if board[0][col]["text"] == playerX:
                player1_score += 1
            else:
                player2_score += 1
            score_label.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")

            label.config(text=winner_name + " wins!", foreground=color_blue)
            for row in range(3):
                board[row][col].config(foreground=color_blue, background=color_red)
            game_over = True
            return

    #diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        winner_name = player1_name if board[0][0]["text"] == playerX else player2_name

        if board[0][0]["text"] == playerX:
            player1_score += 1
        else:
            player2_score += 1
        score_label.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")

        label.config(text=winner_name + " wins!", foreground=color_blue)
        for i in range(3):
            board[i][i].config(foreground=color_blue, background=color_red)
        game_over = True
        return

    #anti-diagonally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        winner_name = player1_name if board[0][2]["text"] == playerX else player2_name

        if board[0][2]["text"] == playerX:
            player1_score += 1
        else:
            player2_score += 1
        score_label.config(text=f"{player1_name}: {player1_score}   {player2_name}: {player2_score}")

        label.config(text=winner_name + " wins!", foreground=color_blue)
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

def set_names():
    global player1_name, player2_name
    if name_entry1.get().strip() !="":
        player1_name = name_entry1.get().strip()
    if name_entry2.get().strip() !="":
        player2_name = name_entry2.get().strip()
    label["text"] = player1_name + "'s turn (X)"

#game setup
playerX = "X"
playerO = "O"
curr_player = playerX
player1_name = "player 1"
player2_name = "player 2"
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#3b83bd"
color_red = "#e74c3c"
color_dark_grey = "#2c3e50"

turns = 0
game_over = False
player1_score = 0
player2_score = 0

#window setup
window = tkinter.Tk()  # create the game window
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player + "'s turn", font=("Consolas", 20), background=color_dark_grey,
                       foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

# --- ADD THIS BLOCK HERE ---
name_frame = tkinter.Frame(window)
name_frame.pack(pady=10)

score_frame = tkinter.Frame(window)
score_frame.pack(pady=5)

score_label = tkinter.Label(score_frame, text="Player 1: 0   Player 2: 0", 
                             font=("Consolas", 14), background=color_dark_grey, foreground="white")
score_label.grid(row=0, column=0)

tkinter.Label(name_frame, text="Player 1 (X):", background=color_dark_grey, foreground="white").grid(row=0, column=0, padx=5)
name_entry1 = tkinter.Entry(name_frame, width=12)
name_entry1.grid(row=0, column=1, padx=5)

tkinter.Label(name_frame, text="Player 2 (O):", background=color_dark_grey, foreground="white").grid(row=1, column=0, padx=5)
name_entry2 = tkinter.Entry(name_frame, width=12)
name_entry2.grid(row=1, column=1, padx=5)

start_button = tkinter.Button(name_frame, text="Start", command=set_names)
start_button.grid(row=2, column=0, columnspan=2, pady=5)
# --- END BLOCK ---

for row in range(3):
    for col in range(3):
        board[row][col] = tkinter.Button(frame, text="", font=("Consolas", 40, "bold"),
                                         background=color_dark_grey, foreground="white", width=5, height=1,
                                         command=lambda row=row, col=col: set_tile(row, col))
        board[row][col].grid(row=row + 1, column=col)

        board[row][col].bind("<Enter>", lambda e, b=board[row][col]: on_enter(e, b))
        board[row][col].bind("<Leave>", lambda e, b=board[row][col]: on_leave(e, b))

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
