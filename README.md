# Tic-Tac-Toe

**Group Members:** tangmingguang, Marin Wathna, Mony Thi_Radeth, Inn Pongwathnak, Ky Rath Tevy, Keomoniroath, Yi Oun, Vattanakbandid, Heng Piseth, Kosamak

## Description

This project is a two-player Tic-Tac-Toe game built with Python's `tkinter` library. Players take turns clicking on a 3x3 grid to place their mark ("x" or "o"). The game automatically detects wins (rows, columns, diagonals) and ties, highlights the winning line in green, and lets players start a new game with the "restart" button.

## Prerequisites & Installation

- **Python 3** must be installed on your machine.
  - Check your version by running:
    ```
    python3 --version
    ```
  - Download Python from [python.org](https://www.python.org/downloads/) if you don't have it.

- **tkinter** is required for the graphical interface.
  - It comes pre-installed with Python on Windows and macOS.
  - On Linux, install it with:
    ```
    sudo apt install python3-tk
    ```

No other external packages are needed — the project only uses Python's built-in `tkinter` and `random` modules.

## How to Run

1. Clone this repository:
   ```
   git clone https://github.com/minggua/tic-ta-to.git
   ```
2. Navigate into the project folder:
   ```
   cd tic-ta-to
   ```
3. Run the game:
   ```
   python3 src/tictactoe.py
   ```
4. A game window will open. Click any square to place your mark. The current player's turn is shown at the top. Click **restart** at any time to reset the board.

## Repository Structure

```
├── src/
│   └── tictactoe.py     # Main game source code
├── docs/                 # (Optional) additional documentation/diagrams
└── README.md             # Project overview (this file)
```
