from Snake import Snake
from Member import Member


# lists
listofmembers = list()
listofsnakes = list()


# add member method
def addMember() :
    print("What is the name of the member?")
    # user inputs new MEMBER NAME here
    membername = input() 
    m = Member(membername, membername)
    # opens mymembers.txt file
    fw = open("mymembers.txt", "a")
    fw.write("\nMember id: " + str(m.getMemberNumber()) + ". Member name: " + m.getMemberName() + ".")
    fw.close()
    # confirmation that new member has been added
    print("MEMBER ADDED SUCCESSFULLY")
    # Y/N option to continue chosing options without having to break out of terminal
    while True:
        again = input("Add more members? Y/N: ").lower()
        if (again == "y"):
            addMember()
        elif (again == "n"):
            break
        else:
            print("Enter Y or N")
            continue
        break


# add snake method
def addSnake():
    print("What is the name of the snake?")
    # user inputs new SNAKE NAME here
    snakename = input() 
    while True:
        print("What type of snake is it? \" Mamba\" or \"Anaconda\"?")
        # user inputs new SNAKE TYPE here
        snaketype = input() 
        if (snaketype.lower() == "anaconda"):
            print("Whoops. Bad news! This type of snake is protected, and cannot be added!")
            continue
        elif (snaketype.lower() == "mamba"):
            break
        else:
            print("Hmm.. Don't know that type of snake.. Try again with another type of snake.")
            continue
        break
    print("Who is the owner of the snake?")
    # user inputs MEMBER NAME here
    snakeowner = input()
    s = Snake(snakename, snaketype, snakeowner)
    # opens mysnakes.txt file 
    fw = open("mysnakes.txt", "a") 
    fw.write("\nSnake id: " + str(s.getSnakeNumber()) + ". Snake name: " + s.getSnakeType() + ". Snake type: " + s.getSnakeName() + ". Owner of the snake: " + str(s.getMember()) + ".")
    fw.close()
    # confirmation that new snake has been added
    print("SNAKE ADDED SUCCESSFULLY")
    # Y/N option to continue chosing options without having to break out of terminal
    while True:
        again = input("Add more snakes? Y/N: ").lower()
        if (again == "y"):
            addSnake()
        elif (again == "n"):
            break
        else:
            print("Enter Y or N")
            continue
        break

# output options with methods from above that are called based on user selection/input
print("Welcome to the \"Friends of a snake\" association!")
while True:
    print("Press a number to proceed")
    print("Press 1 if you would like to add a member, \nPress 2 if you would like to add a snake, \nPress 3 if you would like to see the list of members, \nPress 4 if you would like to see the list of snakes, \nPress 0 if you want to break free.")
    while True:
        snake_or_member = input()
        try:
            snake_or_member = int(snake_or_member)
        except:
            print("Sorry I didn't get that. You have to enter a number between 0 and 4 to make a choice.")
            continue
        if (snake_or_member == 1):
            print()
            print("ADD A NEW MEMBER")
            addMember()
        elif (snake_or_member == 2):
            print()
            print("ADD A NEW SNAKE")
            addSnake()
        elif (snake_or_member == 3):
            print()
            print("LIST OF MEMBERS")
            # open file in reading mode to see list
            f = open("mymembers.txt", "r")
            print(f.read())
            print()
        elif (snake_or_member == 4):
            print()
            print("LIST OF SNAKES")
            # open file in reading mode to see list
            f = open("mysnakes.txt", "r")
            print(f.read())
            print()
        elif (snake_or_member == 0):
            exit(0)
        else:
            print("You can only enter the numbers 0-4. Try again.")
            continue
        break
    continue