command = ""
started = False

while True:
    command = input('> ').lower()
    if command == "menu":
        print('''
start - to start the car
stop - to stop the car
quit - to quit
                ''')
    elif command == "start":
        if started:
            print("Car is already started!!")
        else:
            started = True
            print("Car started!!")
    elif command == "stop":
        if not started:
            print("Car is already stopped!!")
        else:
            started = False
            print("Car stopped!!")
    elif command == "quit":
        print("Thanks for playing the car game!!")
        break
    else:
        print("Sorry, I don't understand that!!")

