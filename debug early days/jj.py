import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    read = random.randint(0, len(cards) - 1)
    random_card = int(cards[read])
    return random_card

user_cards = []
computer_cards = []
for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculate_score(cards):
    total = sum(cards)
    if "11" in cards and "10" in cards:
        total = 0
    if "11" in cards and total > 21:
        cards.remove(11)
        cards.append(1)
        
    return total

intw = calculate_score(user_cards)
print(intw)
    





