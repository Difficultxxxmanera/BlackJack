import random

def create_deck(): 
    deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    
    random.shuffle(deck)
    return deck

def deal_card(deck):
    return deck.pop()

def calculate_score(cards):
    score = 0
    has_ace = False
    
    for card in cards:
        rank = card[0]
        
        if rank == 'A':
            score += 11
            has_ace = True
        elif rank in ['K', 'Q', 'J']:
            score += 10
        else:
            score += int(rank)
    
    if has_ace and score > 21:
        score -= 10
    
    return score

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    deck = create_deck()
    
    for _ in range(2):
        user_cards.append(deal_card(deck))
        computer_cards.append(deal_card(deck))
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_continue = input("Type 'y' to get another card, or 'n' to pass: ")
            
            if should_continue == 'y':
                user_cards.append(deal_card(deck))
            else:
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(deck))
        computer_score = calculate_score(computer_cards)
    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose!"
    
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer has blackjack. You lose!"
    elif user_score == 0:
        return "You have blackjack. You win!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

play_game()
