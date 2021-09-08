command = ""
started = False
while True:
   command=input(">").lower()
   if command == "start":
       if started:
           print("Car is already on.")
       else:
           started = True
           print("Car is on.")
   elif command =="stop":
       if not started:
           print("car is already stoped")
       else:
           started = False
           print("Car is stopped")
   elif command == "help":
       print(""" start - to start car\nstop - to stop car\nquit - to off car """)
   elif command == "quit":
        break
   else :
    print("I dont understand")