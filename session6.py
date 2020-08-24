import random

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']


## Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck  

deck =  sum(list(map(lambda x : list(zip([x]*13,vals)), suits)),[])

## Write a normal function without using lambda, zip, and map function to create 52 cards in a deck

def Deck(vals,suits):
    """
    This functions will create a deck of 52 cards.
    vals  : ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits : 'spades', 'clubs', 'hearts', 'diamonds']
    """
    deck = []  
    for val in vals:
        for suit in suits:
            deck.append((suit,val))
    
    return(deck)
    
def Game(number_of_cards ,deck):
    
    player1 = []
    player2 = []
    cache = []
    
    # Randomly distributing cards to players
    while (len(player1) != number_of_cards) and (len(player2) != number_of_cards) :
        
        # Getting card for player 1
        index = random.randint(0,51)
        if (index not in cache) and (len(player1) != number_of_cards):
            player1.append(deck[index])
            
        # Getting card for player 2
        index = random.randint(0,51)
        if (index not in cache) and (len(player2) != number_of_cards):
            player2.append(deck[index])
            
    return(player1,player2)
            
player1 = [('spades', 'ace'),
  #('diamonds', '10'),
  ('clubs', '6'),
  #('spades', '9'),
  ('spades', '8')]

player2 = [('spades', 'ace'),
  #('spades', '10'),
  ('spades', 'king'),
  #('spades', 'jack'),
  ('spades', 'queen')]

#player2 = [('spades', '2'),
 # ('hearts', 'jack'),
  #('spades', '9'),
  #('hearts', '3'),
  #('diamonds', 'jack')]
  
def Poker(player1, player2 , number_of_cards):
    
    ### Testing either of players have Royal Flush
    ## Condition : 1. All cards belong to same suit
    ##             2. Cords must be of highest order  '10', 'jack', 'queen', 'king', 'ace'

    ###########################################################################################################################
    ############################################### Testing for Royal Flushes #############################################
    ###########################################################################################################################
    
    card_rank = {
            '2' : 12,
            '3' : 11,
            '4' : 10,
            '5' : 9,
            '6' : 8,
            '7' : 7,
            '8' : 6,
            '9' : 5,
            '10': 4,
            'jack' : 3,
            'queen' : 2,
            'king' : 1,
            'ace' : 0
            }
    Royal_Flush_Cards = ['ace','king','queen','jack','10']
    player1 = sorted(player1,key = lambda val : card_rank[val[1]])
    player2 = sorted(player2,key = lambda val : card_rank[val[1]])
    
    Royal_Flush_player1 = (len((set([suit[0] for suit in player1]))) == 1) and set([val[1] for val in player1]) == set(Royal_Flush_Cards[:number_of_cards])
    Royal_Flush_player2 = (len((set([suit[0] for suit in player2]))) == 1) and set([val[1] for val in player2]) == set(Royal_Flush_Cards[:number_of_cards])
    
    print("################# Royal_Flush ######################")
    print(Royal_Flush_player1,Royal_Flush_player2)
    
    
    
    
    
    ###########################################################################################################################
    ############################################### Testing for Straight Flushes #############################################
    ###########################################################################################################################
    """
    Five cards of the same suit in sequence - such as clubJ-club10-club9-club8-club7. 
    Between two straight flushes, the one containing the higher top card is higher. 
    An ace can be counted as low, so heart5-heart4-heart3-heart2-heartA is a straight flush, 
    but its top card is the five, not the ace, so it is the lowest type of straight flush. 
    The cards cannot "turn the corner": diamond4-diamond3-diamond2-diamondA-diamondK is not valid.
    """     

    card_rank_straight_flush = {
        'ace' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        '10': 10,
        'jack' : 11,
        'queen' : 12,
        'king' : 13
        }
    Straight_Flush_Cards = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    player1 = sorted(player1,key = lambda val : card_rank_straight_flush[val[1]] , reverse = True )
    player2 = sorted(player2,key = lambda val : card_rank_straight_flush[val[1]] , reverse = True)

    # Top Card player 1
    if (len((set([suit[0] for suit in player1]))) == 1):
        
        Top_card_player1 = player1[0][1]
        Straight_Flush_Player1 = set([val[1] for val in player1]) == set(Straight_Flush_Cards[card_rank_straight_flush[Top_card_player1] - number_of_cards : card_rank_straight_flush[Top_card_player1]])
        print("Straight_Flush_Player1 : ",Straight_Flush_Player1)
    # Top Card player 2
    if (len((set([suit[0] for suit in player2]))) == 1):
        
        Top_card_player2 = player2[0][1]
        Straight_Flush_Player2 = set([val[1] for val in player2]) == set(Straight_Flush_Cards[card_rank_straight_flush[Top_card_player2] - number_of_cards : card_rank_straight_flush[Top_card_player2]])
        print("Straight_Flush_Player2 : ",Straight_Flush_Player2)
   
    
        
    ###########################################################################################################################
    ############################################### Testing for Four of a Kind ################################################
    ######################################## Or we can say ALL of a kind in case of 3 and 4 cards #############################
    ###########################################################################################################################
    
    """Four cards of the same rank - such as four queens. The fifth card can be anything.
    This combination is sometimes known as "quads", and in some parts of Europe it is called a "poker", 
    though this term for it is unknown in English. Between two fours of a kind, the one with the higher 
    set of four cards is higher - so 3-3-3-3-A is beaten by 4-4-4-4-2. It can't happen in standard poker, 
    but if in some other game you need to compare two fours of a kind where the sets of four cards are of
    the same rank,then the one with the higher fifth card is better."""
    
    if number_of_cards == 3 or number_of_cards == 4:
        All_of_a_kind_player1 = len((set([val[1] for val in player1]))) == 1
        All_of_a_kind_player2 = len((set([val[1] for val in player2]))) == 1
        print("ALL/Four of a Kind : ")  
        print(All_of_a_kind_player1,All_of_a_kind_player2)
    else:
        Four_of_a_kind_player1 = len((set([val[1] for val in player1]))) == 2
        Four_of_a_kind_player2 = len((set([val[1] for val in player2]))) == 2
        print("ALL/Four of a Kind : ") 
        print(Four_of_a_kind_player1,Four_of_a_kind_player2)
        
    ###########################################################################################################################
    ############################################### Testing for Four of a Kind ################################################
    ######################################## Or we can say ALL of a kind in case of 3 and 4 cards #############################
    ###########################################################################################################################
        
        
    
    
