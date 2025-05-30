import random

print("""
Welcome to the Dice Rolling Simulator!
--------------------------------------
These are your available options:
D4
D6
D8
D10
D12
D16
D20
--------------------------------------
""")

dice_list = [4, 6, 8, 10, 12, 16, 20] # list of available types of dices
answers = ['yes', 'no', 'history'] # list of available answers

# User answers with an invalid amount of sides
def invalid_input(dice_type):
    print("The amount of sides you entered is invalid. Please type in a valid option.")
    print("")

# Checks if user answers with a valid amount of sides
def valid_input(dice_type):

    if dice_type in dice_list:
        return True
    return False

# Checks if user's yes/no answer is valid
def valid_yes_no(continue_game):

    if continue_game in answers:
        return True
    return False

# Warns user's answer is invalid
def invalid_yes_no(continue_game):
    if continue_game not in answers:
        print("Your answer is invalid. Please type in (yes) or (no).")
        print("")
    return

# Roll reaction based on rolled total
def roll_reactions(roll_total):
    if roll_total >= 30:
        print("Wow! That's a pretty good roll!")
    elif roll_total >= 15:
        print("Nice roll! Not too bad")
    elif roll_total >= 10:
        print("Good job!")
    elif roll_total < 10:
        print("Phew! Maybe your roll will be better next time.")

run = True
def main():

    roll_history = []

    while run:

        # User picks die-Type
        dice_type = int(input("How many sides does your die have?: D-"))
        if not valid_input(dice_type):
            invalid_input(dice_type)
            print("")
            continue

        # User determines amount of dices to roll
        dice_num = int(input("Enter number of dices that are going to be rolled: "))

        # Initializes roll of die / dices
        roll_num = random.randint(1, dice_type)
        random_mod = random.random()
        roll_total = round((roll_num * dice_num) + random_mod)

        # Store roll
        roll_history.append(roll_total)

        print("You just rolled: " + str(roll_total))

        # Extension for roll reactions
        roll_reactions(roll_total)

        # Path-options
        while True:
            continue_game = input("Would you like to roll again (yes / no) or see your roll log (history)?: ")
            print("")
            if valid_yes_no(continue_game):
                if continue_game == 'history':
                    print("Roll history: ", roll_history)  # Step 3: Display history
                    print("--------------------------------------")
                    print("")
                elif valid_yes_no(continue_game):
                    if continue_game == 'yes':
                        print("--------------------------------------")
                        break
                    elif continue_game == 'no':
                        return
                else:
                    invalid_yes_no(continue_game)

if __name__ == '__main__':
    main()
