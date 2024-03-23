import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_cards():
player_card_one = random.choice(cards)
player_card_two = random.choice(cards)
dealer_card_one = random.choice(cards)
dealer_card_two = random.choice(cards)
players_cards = [player_card_one,player_card_two]
dealers_cards = [dealer_card_one,dealer_card_two]
return players_cards, dealers_cards

players_cards, dealers_cards = deal_cards()

def final_score(dealt_cards):
return sum(dealt_cards)

def another_card(current_cards,deck):
generate_card = random.choice(deck)
current_cards = current_cards.append(generate_card)
return current_cards

def is_bust(cards_total):
return final_score(cards_total) > 21

def is_blackjack(players_cards,dealers_cards):
players_score = final_score(players_cards)
dealers_score = final_score(dealers_cards)
if players_score == 21 and dealers_score == 21:

   return "Double blackjack - it's a draw!"
elif players_score == 21:
    return "You win!"
elif dealers_score == 21:
    return "Dealer wins"
else:
    return "No blackjack"

result = is_blackjack(players_cards,dealers_cards)
if result == "No blackjack":
print(f"Your cards are {players_cards}")
print(f"Dealers cards are {dealers_cards[0]}, *")

players_go = True
dealers_go = True

while players_go:
print(f"Players cards: {players_cards}. Players total: {final_score(players_cards)}")
hit = input("Would you like to hit or stick")
if hit == "h":
another_card(players_cards,cards)
if is_bust(players_cards):
for i in range(len(players_cards)):
if players_cards[i] == 11:
print(f"Adjusting ace...")
players_cards[i] = 1
if not is_bust(players_cards):
print(f"New score: {final_score(players_cards)}")
break
else:
print("bust")
print("You lose!")
print(f"Players final score: {final_score(players_cards)}")
print(f"The dealers score: {final_score(dealers_cards)}")
players_go = False
dealers_go = False

       else:
           players_go = False

while dealers_go:
print(f"Dealers cards: {dealers_cards}. Dealer Total: {final_score(dealers_cards)}")
if final_score(dealers_cards) < 17:
another_card(dealers_cards, cards)
print(f"Dealer drew a: {dealers_cards}")
if is_bust(dealers_cards):
print("Dealer bust! You win,")
print(f"Players final score: {final_score(players_cards)}")
print(f"The dealers score: {final_score(dealers_cards)}")
dealers_go = False
elif final_score(dealers_cards) <= 21:
print(f"Players final score: {final_score(players_cards)}")
print(f"The dealers score: {final_score(dealers_cards)}")
else:
if final_score(players_cards) > final_score(dealers_cards) and final_score(players_cards) <= 21:
print("You win!")
else:
print("House wins!")
dealers_go = False

print(f"Players final score: {final_score(players_cards)}")
print(f"The dealers score: {final_score(dealers_cards)}")
