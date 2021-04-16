import psphelper
import random


# NORMAL DICE ROLL FUNCTION
def dice_roll():
    dice = random.randint(1, 4)
    return dice


diceroll = [dice_roll(), dice_roll(), dice_roll(), dice_roll(), dice_roll()]  # dice roll


# SPECIFIC DICE ROLL FUNCTION
def specific_roll(playerRoll, diceroll):
    for i in playerRoll and range(max(element) + 1):  # playerRoll from element
        diceroll[i] = random.randint(1, 4)  # rolling specific dice based on range
    return diceroll


# USER INPUT OPTIONS FUNCTION
# STANDARDIZING THE INPUT
# SPLITTING THE INPUT BASED ON INDICES TO DIFFERENTIATE THE COMMAND AND DICE OPTIONS
def inputOptions():
    while True:
        input_options = input("Input > ").upper().split(" ")
        acceptCase = ["ROLL", "CHEAT", "SAVE"]
        if not input_options or input_options[0] not in acceptCase:
            pass  # show invalid input and print user input again
        option = input_options[0]
        element = [] if len(input_options) == 1 else input_options[1:len(input_options)]  # get list from string
        # SAVE AND NORMAL ROLL
        if option == "SAVE" or option == "ROLL" and not element:
            return option, element
        # SPECIFIC DICE ROLL
        elif option == "ROLL":
            element = ListToIntRoll(element, 0, 4)  # converting string in list to integer
            if element[i] in range(4):
                return option, element
        # CHEAT
        elif option == "CHEAT" and len(element) == 5:
            element = ListToIntCheat(element, 1, 4)  # converting string in list to integer
            if element:
                return option, element
        print("ERROR: Invalid input.")  # print if wrong input from user


# LIST TO INTEGER CONVERSION FUNCTION FOR SPECIFIC ROLL
def ListToIntRoll(element, minVal, maxVal):
    try:
        element = [int(i) + (-1) for i in element]  # convert string to integer
    except ValueError:
        return False

    if min(element) >= minVal: return element  # determining minimum value
    if max(element) <= maxVal: return element  # determining maximum value

    else:
        return False


# LIST TO INTEGER CONVERSION FUNCTION FOR CHEAT FUNCTION
def ListToIntCheat(element, minVal, maxVal):
    try:
        element = [int(i) for i in element]  # converting string to integer
    except ValueError:
        return False

    if min(element) >= minVal: return element  # determining minimum value
    if max(element) <= maxVal:
        return element  # determining maximum value

    else:
        return False


# DICE COUNT BASED ON CATEGORY
# PUTTING THE RANDOM DICE IN LIST, AND USING THE COUNT ATTRIBUTE TO DETERMINE THE DICE NUMBER
def dC(diceroll):
    count = list([diceroll.count(i) for i in range(1, 5)])
    # dicecount for 1s, 2s, 3s, 4s
    oneS = count[0] * 1
    twoS = count[1] * 2
    threeS = count[2] * 3
    fourS = count[3] * 4

    # dicecount for trio and quartet
    maxCount = max(count)
    sumDice = sum(diceroll)

    if maxCount >= 4:
        quartet = trio = sumDice
    elif maxCount == 3:
        trio = sumDice
        quartet = 0
    else:
        trio = quartet = 0

    # dicecount for doremi
    doremi = 20
    if 0 in count:
        doremi = 0

    # dicecount for band
    band = 0
    if 2 in count and 3 in count:
        band = 30

    # dicecount for orchestra
    orchestra = 0
    if 5 in count:
        orchestra = 40

    return [oneS, twoS, threeS, fourS, trio, quartet, doremi, band, orchestra]  # return score


# FORMING THE TABLE

scoreboard = [
    [None, None, None, None, None, None, None, None, None],  # player 1
    [None, None, None, None, None, None, None, None, None],  # player 2
]

playerRow = ["Player 1", "Player 2"]
categoryColumn = ["1S", "2S", "3S", "4S", "Trio", "Quartet", "Band", "Doremi", "Orchestra"]

total = [0, 0]  # totalscore

# INTERFACE
# USING FOR LOOP TO MAKE SURE THAT THE GAME ENDS AFTER ROUND 18
for i in range(19):
    # TITLE
    title = "Battle of the Sexes (B.O.T.S)"
    fillchar = "="
    print(title.center(80, fillchar))
    # DISPLAY SCOREBOARD
    psphelper.ShowTableByList("Scoreboard", playerRow, categoryColumn, scoreboard)
    print(f"Player 1:{total[0]}")
    print(f"Player 2:{total[1]}")
    print()

    if i == 18:
        break  # game ends when 18 rounds

    # SWAPPING PLAYER TURN
    playerTurn = i % 2  # 0 for player 1, 1 for player 2
    print(f"Player {playerTurn + 1}")
    print("========")
    input("Press ENTER to roll dice.")
    print()

    # A LIST TO DETERMINE THE DICE NUMBER FOR SPECIFIC DICE ROLLING
    # USING FOR LOOP TO MAKE SURE THAT EACH PLAYER DOES NOT EXCEED 3 ROUNDS
    playerRoll = []
    for rollNum in range(1, 4):
        if playerRoll:  # if playerRoll has elements
            diceroll = specific_roll(playerRoll, diceroll)  # perform specific dice roll
        else:
            diceroll = [dice_roll(), dice_roll(), dice_roll(), dice_roll(), dice_roll()]  # reroll all dice

        print(f"Roll #{rollNum} :", diceroll)
        print()
        scoreResult = dC(diceroll)  # obtain score result
        finalScore = [scoreResult]
        psphelper.ShowTableByList("Category Scores", [], categoryColumn, finalScore)  # display scores

        if rollNum == 3:
            break  # skip input when third roll

        print("Input Options: ")
        print("\tSAVE           :- Accept these dice.")
        print("\tROLL           :- Re-roll ALL dice.")
        print("\tROLL d1 ... dn :- Re-roll specified dice only.\n")

        option, element = inputOptions()  # obtain input from function inputOptions
        if option == "SAVE":
            break  # end loop and proceed to enter category choice
        elif option == "ROLL":  # normal roll and specific roll
            playerRoll = element
        elif option == "CHEAT":
            scoreResult = dC(element)  # update score with number from cheat command
            finalScore = [scoreResult]
            psphelper.ShowTableByList("Category Scores", [], categoryColumn, finalScore)  # display score
            break  # end loop

    # AFTER CHEAT, SAVE AND THE THIRD ROLL,
    # PROGRAM WILL AUTOMATICALLY BREAK FROM THE FOR LOOP TO ASK FOR CATEGORY INPUT TO SAVE THE SCORE
    while True:
        input_category = input("Enter your desired category: ")
        category = input_category.title()
        if category not in categoryColumn:
            print("ERROR: Input invalid.")
            continue  # user input to choose category again
        scoreIndex = categoryColumn.index(category)  # determine category index
        score = scoreResult[scoreIndex]  # determine score index
        if scoreboard[playerTurn][scoreIndex] is None:
            total[playerTurn] += score  # add score to totalscore
            scoreboard[playerTurn][scoreIndex] = score  # add score to scoreboard
            break
        print(f"ERROR: Category '{input_category}' has been used.")  # loop runs again and user input again

    # CLEAR COMMAND PROMPT SCREEN AFTER EACH PLAYER
    psphelper.ClearScreen()

# DETERMINE THE FINAL SCORE AND WINNER

if total[0] > total[1]:
    input("Player 1 wins!")
elif total[0] < total[1]:
    input("Player 2 wins!.")
else:
    input("It's a tie!")