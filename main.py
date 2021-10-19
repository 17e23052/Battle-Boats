from time import sleep
def menu():
  print("Option 1 = New game")
  print("Option 2 = Resume game")
  print("Option 3 = Instructions")
  print("Option 4 = Quit")
  option = input("Enter option number: ")
  if option == "1":
    newgame() #This starts a new game
  elif option == "2":
    resumegame() #This resumes the previous saved game
  elif option == "3":
    instructions() #This opens the instructions
    menu()
  elif option == "4":
    print("Thanks for playing! Come again another time!") #This ends the code with a goodbye message
  else:
    print("Invalid input.")
    menu() #Reruns the menu code if the input was invalid

def displayboard(board):
  print(" ", "A", "│", "B", "│", "C", "│", "D", "│", "E", "│", "F", "│", "G", "│", "H")
  print(" ───┼───┼───┼───┼───┼───┼───┼──")
  print("1", board[0][0], "│", board[0][1], "│", board[0][2], "│", board[0][3], "│", board[0][4], "│", board[0][5], "│", board[0][6], "│", board[0][7])
  print(" ───┼───┼───┼───┼───┼───┼───┼──")
  print("2", board[1][0], "│", board[1][1], "│", board[1][2], "│", board[1][3], "│", board[1][4], "│", board[1][5], "│", board[1][6], "│", board[1][7])
  print(" ───┼───┼───┼───┼───┼───┼───┼──")
  print("3", board[2][0], "│", board[2][1], "│", board[2][2], "│", board[2][3], "│", board[2][4], "│", board[2][5], "│", board[2][6], "│", board[2][7])
  print(" ───┼───┼───┼───┼───┼───┼───┼──")
  print("4", board[3][0], "│", board[3][1], "│", board[3][2], "│", board[3][3], "│", board[3][4], "│", board[3][5], "│", board[3][6], "│", board[3][7])
  print(" ───┼───┼───┼───┼───┼───┼───┼──")
  print("5", board[4][0], "│", board[4][1], "│", board[4][2], "│", board[4][3], "│", board[4][4], "│", board[4][5], "│", board[4][6], "│", board[4][7])
  print(" ───┼───┼───┼───┼───┼───┼───┼──")
  print("6", board[5][0], "│", board[5][1], "│", board[5][2], "│", board[5][3], "│", board[5][4], "│", board[5][5], "│", board[5][6], "│", board[5][7])
  print(" ───┼───┼───┼───┼───┼───┼───┼──")
  print("7", board[6][0], "│", board[6][1], "│", board[6][2], "│", board[6][3], "│", board[6][4], "│", board[6][5], "│", board[6][6], "│", board[6][7])
  print(" ───┼───┼───┼───┼───┼───┼───┼──")
  print("8", board[7][0], "│", board[7][1], "│", board[7][2], "│", board[7][3], "│", board[7][4], "│", board[7][5], "│", board[7][6], "│", board[7][7])
  print(" ───┼───┼───┼───┼───┼───┼───┼──")

def empty_board(player):
  file = open(f"battleboat{player}.csv", "w")
  grid = [[" ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "]]
  data = ""
  for line in grid:
    for item in line:
      data = data + item + ","
    data = data + "\n"
  file.write(data) #Writing the data to the board
  file.close()

def newgame():
  empty_board("P1")
  empty_board("P2")
  print("Welcome to battle boats!")
  sleep(1)
  print("Here is the grid layout. This is your fleet grid:")
  sleep(1)
  empty_board("P1")
  file = open("battleboatP1.csv","r")
  data = []
  for line in file:
    line = line.strip("\n")
    line = line.split(",")
    data.append(line)
  displayboard(data) #This displays the grid layout
  sleep(3)
  print("Enter your five boat locations:")
  check_space()
  check_space()
  check_space()
  check_space()
  check_space()

def check_space():
  boat = input().upper()
  for letter in boat:
    if letter == "A":
      letter2 = 1
    elif letter == "B":
      letter2 = 2
    elif letter == "C":
      letter2 = 3
    elif letter == "D":
      letter2 = 4
    elif letter == "E":
      letter2 = 5
    elif letter == "F":
      letter2 = 6
    elif letter == "G":
      letter2 = 7
    elif letter == "H":
      letter2 = 8
    elif letter == "1":
      letter1 = 1
    elif letter == "2":
      letter1 = 2
    elif letter == "3":
      letter1 = 3
    elif letter == "4":
      letter1 = 4
    elif letter == "5":
      letter1 = 5
    elif letter == "6":
      letter1 = 6
    elif letter == "7":
      letter1 = 7
    elif letter == "8":
      letter1 = 8

def resumegame():
  print("Work in progress LOL")
  print()
  menu()

def instructions():
  print('''Battle boats is a turn based strategy game where players eliminate their opponents fleet of boats by
  ‘firing’ at a location on a grid in an attempt to sink them. The first player to sink all of their
  opponents’ battle boats is declared the winner. 

Each player has two eight by eight grids. One grid is used for their own battle boats and the other is
used to record any hits or misses placed on their opponents. At the beginning of the game, players decide where they wish to place their fleet of five battle boats. 

During game play, players take it in turns to fire at a location on their opponents board. They do this by stating the coordinates for their target. If a player hits their opponent's boat then this is recorded as a hit. If they miss then this is recorded as a miss. 

The game ends when a player's fleet of boats have been sunk. The winner is the player with boats remaining at the end of the game.
''')


menu()