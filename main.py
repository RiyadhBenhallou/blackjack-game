from random import choice
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return choice(cards)

def formatted_dealer_cards(cards):
    list = []
    for i in range(len(cards) - 1):
        list.append(cards[i])
    list.append('*')
    return list

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def continue_playing():
    global user_score, computer_score

    user_cards.append(deal_card())
    user_score = calculate_score(user_cards)
    print(f'Your cards are: {user_cards}, current score: {user_score}')

    if user_score > 21:
        print('You lose')
        game_over()
        return

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'Computer\'s cards are: {formatted_dealer_cards(computer_cards)}')

    if computer_score > 21:
        print('Dealer busts, you win')
        game_over()
        return
    elif computer_score == 21:
        print('Blackjack, dealer wins')
        game_over()
        return

    answer = input('Do you want to continue? ')
    if answer.lower() == 'yes':
        continue_playing()
    else:
        if user_score > computer_score:
            print('You win')
        else:
            print('You lose')
        game_over()

def game_over():
    print(f'Your final cards: {user_cards}, final score: {user_score}')
    print(f'Dealer\'s final cards: {computer_cards}, final score: {computer_score}')

user_cards = [deal_card() for _ in range(2)]
computer_cards = [deal_card() for _ in range(2)]

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(logo)

print(f'Your cards are: {user_cards}, current score: {user_score}')
print(f'Computer\'s cards are: {formatted_dealer_cards(computer_cards)}')

if user_score == 21:
    print('Blackjack, you win')
    game_over()
elif computer_score == 21:
    print('Blackjack, you lose')
    game_over()
else:
    answer = input('Do you want to deal another card? ')
    if answer.lower() == 'yes':
        continue_playing()
    else:
        if user_score > computer_score:
            print('You win')
        else:
            print('You lose')
        game_over()
