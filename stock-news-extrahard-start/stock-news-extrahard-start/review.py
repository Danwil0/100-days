import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def initiate():
    start = input("Do you want to play a game of Blacjack?Type 'y' or 'n'")
    if start == 'y':
        blackjack()
    else:
        print("Shoo Away")


def blackjack():
    # Comparison
    def compare(compare_link, play_more):
        if score["players_score"] == 21:
            compare_link["switch"] = True
            compare_link["result"] = "Blackjack! You Win"
            return compare_link
        elif score["computers_score"] == 21:
            compare_link["switch"] = True
            compare_link["result"] = "Blackjack! You Loose"
            return compare_link
        elif score["players_score"] > 21:
            compare_link["switch"] = True
            compare_link["result"] = "You Loose because you overshot 21"
            return compare_link
        elif score["computers_score"] > 21:
            compare_link["switch"] = True
            compare_link["result"] = "You Win because computer overshot 21"
            return compare_link
        elif play_more is False:
            if score["players_score"] > score["computers_score"]:
                compare_link["result"] = "You Win"
                return compare_link
            elif score["players_score"] < score["computers_score"]:
                compare_link["result"] = "You Loose"
                return compare_link
            else:
                compare_link["result"] = "Draw"
                return compare_link

        else:
            compare_link["switch"] = False
            return compare_link

    compare_link = {
        "result": "",
        "switch": False,
    }

    # To Display
    def display(score, playing_cards, play_more):

        if play_more is False:
            print(f"Your final hand: {playing_cards[0]}, final score: {score['players_score']}")
            print(f"Computers final hand: {playing_cards[1]}, final score: {score['computers_score']}")
        elif compare_link["switch"] is True:
            print(f"Your final hand: {playing_cards[0]}, final score: {score['players_score']}")
            print(f"Computers final hand: {playing_cards[1]}, final score: {score['computers_score']}")
        else:
            print(f"Your cards: {playing_cards[0]}, current score: {score['players_score']}")
            print(f"Computer's first card: {playing_cards[1][0]}")

    # Adding card
    def add_card(playing_cards):
        playing_cards[0].append(cards[random.randint(0, 12)])
        playing_cards[1].append(cards[random.randint(0, 12)])
        return playing_cards

    # Scoring
    def scoring(score, playing_cards):
        score["counter"] += 1
        score["players_score"] += playing_cards[0][score["counter"]]
        score["computers_score"] += playing_cards[1][score["counter"]]
        return score

    # Cards in a list
    player_cards = [cards[random.randint(0, 12)]]
    computer_cards = [cards[random.randint(0, 12)]]
    playing_cards = [player_cards, computer_cards]
    # Scores in dictionary
    score = {
        "players_score": playing_cards[0][0],
        "computers_score": playing_cards[1][0],
        "counter": 0,
    }
    play_more = True
    # Adding second card in the very start
    playing_cards = add_card(playing_cards)
    score = scoring(score, playing_cards)
    display(score, playing_cards, play_more)

    # If picking another card
    # compare_link = {
    #   "result": "",
    #   "switch": False,
    # }

    while play_more:
        choice = input("Do you want to choose again?'y'/'n': ")

        if choice == 'y':
            playing_cards = add_card(playing_cards)
            score = scoring(score, playing_cards)
            compare_link = compare(compare_link, play_more)
            if compare_link["switch"] is True:
                display(score, playing_cards, play_more)
                print(compare_link["result"])
                initiate()
                play_more = False
            else:
                display(score, playing_cards, play_more)

        else:
            play_more = False
            display(score, playing_cards, play_more)
            compare_link = compare(compare_link, play_more)
            print(compare_link["result"])


initiate()