# This is the main engine of the game. We should probably try to run most of our code in separate files and consolidate them here.

# 1. Character creation. Alternatively, reading from existing save??
def start_game():
    """
    User has to select whether it's a new game or if they want to load from a save.
    """
    try:
        choice = input("1. New game. 2. Load game. ")
        if choice == 1:
            new_game()
        elif choice == 2:
            load_game()
    except:
        print("Enter the corresponding number.")

def new_game():
    """
    Asks a number of questions and uses the answers to create the player instance.
    """
    pass

def load_game():
    """
    Makes the user select an existing save file. Doesn't have to be the perfect UX.
    """
    pass

# 2. Gameplay loop. Combat, going to town, interacting with NPCs.
