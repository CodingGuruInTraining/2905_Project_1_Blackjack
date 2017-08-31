#   This is the start of a simple Blackjack game.
#
#
# Imports random library
import random
# Imports Class
from Player_Class import Player

def main():
    # Introduction message.
    print("Welcome! Let's play some Blackjack!")
    print("Your score is:")
    # name = input("Name: ")
    name = "Player1"
    dealerName = "Dealer"
    # Creates player objects for both the User and Dealer
    newPlayer = makeNewPlayer(name)
    dealer = makeNewPlayer(dealerName)

    # Start game loop
    gameON = True
    while gameON:
        # Checks whether game is over before it begins
        if checkGameover(newPlayer, dealer) == True:
            gameON = False
            break
        # Inner game loop
        keepPlaying = True
        while keepPlaying:
            # Prompts User to draw or stay
            if drawOrStay(newPlayer.score) == True:
                # Draws card and adds to object.
                drawCards(newPlayer)
                # Checks if score is in the safe zone and not over 21
                safe = checkScore(newPlayer.score)
                if safe == False:
                    keepPlaying = False
                    gameON = False
                    break
                else:
                    # Continues prompt
                    keepPlaying = drawOrStay(newPlayer.score)
            else:
                # Dealer's turn.
                while dealer.score < 17:
                    drawCards(dealer)
                    if checkGameover(newPlayer, dealer) == True:
                        gameON = False
                # End loop
                keepPlaying = False
        # Displays results and ends game loop
        compareScores(newPlayer.score, dealer.score)
        gameON = False



###########################

#####   FUNCTIONS   #######

###########################

# Generates new Player object with 2 starting cards.
def makeNewPlayer(name):
    card1 = random.randint(2, 11)
    card2 = random.randint(2, 11)
    newPlayer = Player(name, card1, card2)
    newPlayer.tallyScore()
    return newPlayer

# Redundant counter that determines if score is or not 21
def checkBlackjack(cards):
    total = 0
    for card in cards:
        total += card
    if total == 21:
        return True
    else:
        return False

# Checks whether game is over
def checkGameover(newPlayer, dealer):
    if checkBlackjack(dealer.cards) == True:
        print("Sorry, dealer has Blackjack")
        return True
    elif checkBlackjack(newPlayer.cards) == True:
        print("Winner, winner, Chicken Dinner!")
        return True
    else:
        return False

# Prompt for User.
def drawOrStay(score):
    print(score)
    if score < 21:
        answer = input("Press D to Draw or S to Stay")
        if answer == "d" or answer == "D":
            return True
        elif answer == "s" or answer == "S":
            return False

# Draws a random number and adds to player object
def getCard(player):
    newCard = random.randint(2, 11)
    player.cards.append(newCard)

# Draws card and tallys up score
def drawCards(player):
    getCard(player)
    player.tallyScore()

# Display function for reaching 21 or going over
def checkScore(score):
    if score == 21:
        print("BLACKJACK!")
        return False
    elif score > 21:
        print("BUST")
        return False
    else:
        return True

# Displays final scores and determines winner
def compareScores(playerScore, dealerScore):
    print("You have " + str(playerScore))
    print("Dealer has " + str(dealerScore))
    if playerScore == dealerScore:
        print("PUSH")
    elif playerScore > dealerScore and playerScore < 22:
        print("You win!")
    elif playerScore < 22 and dealerScore > 21:
        print("Dealer busts. You win!")
    else:
        print("Better luck next time")

# Runs Main function
main()