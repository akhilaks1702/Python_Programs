command = ""
while command != "quit":
    command = input('> ').lower()
    if command == "start":
        print("Car stared!!")
    elif command == "stop":
        print("Car stopped!!")
    elif command == "menu":
        print('''
        start - to start the car
        stop - to stop the car
        quit - to quit
        ''')
    elif command == "quit":
        print("Thanks for playing the car game!!")
        break
    else:
        print("Sorry, I don't understand that!!")

