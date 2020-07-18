
import time

answer = input("What you like to play? (yes/no)")

if answer.lower().strip() == "yes":
    
    answer = input("You reach a crossroads, would you like to left or right?").lower().strip()
    if answer == "left":
        answer = input("You encounter a monster, would you like to run or attack?").lower().strip()

        if answer == "attack":
            print("That was not the greatest idea, you lost!")
        else:
            print("Good choice, you made it away safely.")

    elif answer == "right":
        print("You walk aimlessly to the right and fall on a patch of ice, you injure your leg and cannot continue. Game over")
        for x in range(10, 0, -1):
            print ("The program will be exit after " + str(x))
            time.sleep(1)

    else:
        print("Invalid choice, you lost!")
else:
    print("That's to bad")