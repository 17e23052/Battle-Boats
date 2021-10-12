def menu():
  print("Option 1 = New game")
  print("Option 2 = Resume game")
  print("Option 3 = Instructions")
  print("Option 4 = Quit")
  option = int(input("Enter option number: "))
  if option == 1:
    newgame()
  elif option == 2:
    resumegame()
  elif option == 3:
    instructions()
  elif option == 4:
    print("Thanks for playing! Come again another time!")

menu()