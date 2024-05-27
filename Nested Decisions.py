#1. Nested Decisions:The Adventure Game

place = str (input("Choose a place: Forest or Cave?"))

if place == "Forest":
    action = input("Climb a tree or cross a river?")
    if action == "Climb a tree":
        print("You found a bird's nest!")
    else:
        print ("You found a boat!")
if place == "Cave":
    print("You find a hidden treasure")
            
#Task 2: Setting the scene.

place = str (input("Choose a place: Forest or Cave?"))

if place == "Forest":
    action = input("Climb a tree or cross a river?")
    if action == "Climb a tree":
        print("You found a bird's nest!")
    else:
        print ("You found a boat!")
if place == "Cave":
    action = (input("Light a torch or proceed in the dark?"))
    if action == "Light a torch":
        print("You find a hidden treasure")
    else:
        print ("You stumble in the dark and fall!!")

#Task 3: Default Path

place = str (input("Choose a place: Forest or Cave?"))

if place == "Forest":
    action = input("Climb a tree or cross a river?")
    if action == "Climb a tree":
        pass # will fill in later
    else:
        print ("You found a boat!")
if place == "Cave":
    pass #will fill out later