#Car Game ( No GUI just backend )
# ORIGINAL SOLUTION
command = ""
started = False
while True: # while command != "quit":
    command = input ("> ").lower () # Showing as a lower case
    if command == "start":
        if started:
            print ("Car is already started")
        else:
            started = True
            print ("Car started...")
    elif command == "stop":
        if not started:
            print ("Cat is already stopped")
        else:
            started = False
            print ("Car stopped.")

    elif command == "help":
        print ("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else: print ("Sorry I dont understand this")

