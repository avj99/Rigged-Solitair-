#----------------------------------------------------
# Assignment 3: Rigged Solitaire
# 
# Author: 
# Collaborators/References:
#----------------------------------------------------

class CardNode:
    VALID_SUITS = ['D', 'S', 'H', 'C']
    VALID_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    
    
    # DO NOT CHANGE __init__ method
    def __init__(self, rank, suit, faceUp = True):
        '''
        Initializes a doubly linked list node that stores information about a card. 
        Cards have a suit and rank, and may be face up or down. Asserts that the provided
        suit and rank are valid.

        Input:
          - rank (string): represents number 2-10, Jack, Queen, King, Ace
          - suit (string): represents spade, heart, diamond, or club
          - faceUp (Boolean): represents whether the card is face up (True) or face down (False)

        Returns: None
        '''        
        assert type(rank) == str, "Rank must be a string"
        assert type(suit) == str, "Suit must be a string"
        assert type(faceUp) == bool, "Visible must be boolean"
        
        assert len(suit) == 1, 'Suit must be a single character'
        assert len(rank) == 1, 'Rank must be a single character'
        
        suit = suit.upper()
        rank = rank.upper()
        assert (suit in CardNode.VALID_SUITS), "Invalid Suit provided: {}.".format(suit)
        assert (rank in CardNode.VALID_RANKS), "Invalid Rank provided: {}.".format(rank)
        
        self.__rank = rank
        self.__suit = suit
        self.__faceUp = faceUp
        self.__next = None
        self.__previous = None
    
    # DO NOT CHANGE getRank method   
    def getRank(self):
        '''Returns the rank of the card. No input.'''
        return self.__rank
    
    # DO NOT CHANGE getSuit method
    def getSuit(self):
        '''Returns the suit of the card. No input.'''
        return self.__suit
    
    # DO NOT CHANGE isFaceUp method
    def isFaceUp(self):
        '''Returns whether the card is face up (True) or down (False). No input.'''
        return self.__faceUp
    
    # DO NOT CHANGE turnOver method
    def turnOver(self):
        '''
        Changes the card from face up to face down, or from face down to face up.
        Input: N/A  
        Returns: None.
        '''
        self.__faceUp = not(self.__faceUp)
      
    # DO NOT CHANGE getNext method    
    def getNext(self):
        '''Returns the reference to whatever is next (either None or a CardNode). No input.'''
        return self.__next
    
    # DO NOT CHANGE setNext method
    def setNext(self, newNext):
        '''
        Updates the next reference.
        Input: newNext (None or a CardNode) - the object that will come next
        Returns: None
        '''        
        assert (isinstance(newNext, CardNode) or newNext==None),\
               'Cannot set next to {}'.format(type(newNext))
        self.__next = newNext
    
    # DO NOT CHANGE getPrevious method    
    def getPrevious(self):
        '''Returns the reference to whatever is previous (either None or a CardNode). No input.'''
        return self.__previous
    
    # DO NOT CHANGE setPrevious method
    def setPrevious(self, newPrevious):
        '''
        Updates the previous reference.
        Input: newPrevious (None or a CardNode) - the object that will come previous
        Returns: None
        '''          
        assert (isinstance(newPrevious, CardNode) or newPrevious == None),\
               'Cannot set next to {}'.format(type(newPrevious))
        self.__previous = newPrevious      
    
    
    def __lt__(self, anotherCardNode):
        # TO DO: delete pass and complete the method
        VALID_SUITS = ['D', 'S', 'H', 'C']
        VALID_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']        
        a= self.__suit
        b= self.__rank
        c=anotherCardNode.__suit
        d=anotherCardNode.__rank
        
        
        if VALID_RANKS.index(b) < VALID_RANKS.index(d):
            return True        
        elif VALID_RANKS.index(b) == VALID_RANKS.index(d) and VALID_SUITS.index(a) < VALID_SUITS.index(c):
            return True
        else:
            return False
       
        
      
        
    def __gt__(self, anotherCardNode):
        # TO DO: delete pass and complete the method
        a= self.__suit
        b= self.__rank
        c=anotherCardNode.__suit
        d=anotherCardNode.__rank
        
        VALID_SUITS = ['D', 'S', 'H', 'C']
        VALID_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        
        if VALID_RANKS.index(b) > VALID_RANKS.index(d):
            return True        
        elif VALID_RANKS.index(b) == VALID_RANKS.index(d) and VALID_SUITS.index(a) > VALID_SUITS.index(c):
            return True
        else:
            return False
       
    def isPreviousRank(self, anotherCardNode):
        # TO DO: delete pass and complete the method
        a= self.__suit
        b= self.__rank
        c=anotherCardNode.__suit
        d=anotherCardNode.__rank
        
        VALID_SUITS = ['D', 'S', 'H', 'C']
        VALID_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
         
        if VALID_RANKS.index(b) < VALID_RANKS.index(d) and VALID_RANKS.index(b)== VALID_RANKS.index(d)-1: # if the 
            return True
        else:
            return False
    
    # DO NOT CHANGE __str__ method         
    def __str__(self):
        '''
        If face up, a string showing the rank and suit of the card will be returned.
        If face down, a string showing the back of the card will be returned.
        Input: N/A
        Returns: string representation of the CardNode
        '''
        s = '['
        if self.__faceUp:
            s += ' ' + self.__rank + self.__suit
        s += ' ]'
        return s


class CardList():
    # DO NOT CHANGE __init__ method
    def __init__(self):
        '''
        Initializes the CardList, which is very similar to a Doubly Linked List.
        A CardList can only have CardNodes and None in its sequence.
        Input: N/A
        Returns: None 
        '''
        self.__head = None  # do not change
        self.__tail = None  # do not change
        self.__size = 0     # do not change
    
    # DO NOT CHANGE getHead method     
    def getHead(self):
        '''Returns head of list (either a CardNode or None). No input.'''
        return self.__head
    
    # DO NOT CHANGE getTail method
    def getTail(self):
        '''Returns tail of list (either a CardNode or None). No input.'''
        return self.__tail
    
    # DO NOT CHANGE getSize method
    def getSize(self):
        '''Returns number of CardNodes in sequence. No input.'''
        return self.__size    
    
    # DO NOT CHANGE add method
    def add(self, cardNode):
        '''
        Adds a CardNode to the beginning (head) of the CardList and updates the size.
        Notice the similarity between this and the Doubly Linked List add method.
        Input: cardNode (must be a CardNode)
        Returns: None
        '''
        temp = cardNode
        temp.setPrevious(None) #make sure node is on its own
        temp.setNext(None)     #make sure node is on its own   
        temp.setNext(self.__head)
        if self.__head != None:  # there is a head
            self.__head.setPrevious(temp)
        else:                    # adding to empty list
            self.__tail=temp
        self.__head = temp
        self.__size += 1 
        

    # DO NOT CHANGE append method
    def append(self, cardNode):
        '''
        Appends a CardNode to the end (tail) of the CardList and updates the size.
        Notice the similarity between this and the Doubly Linked List append method.
        Input: cardNode (must be a CardNode)
        Returns: None
        '''        
        temp = cardNode
        temp.setPrevious(None) #make sure node is on its own
        temp.setNext(None)     #make sure node is on its own
        if (self.__head == None):
            self.__head=temp
        else:
            self.__tail.setNext(temp)
            temp.setPrevious(self.__tail)
        self.__tail=temp
        self.__size +=1  
    
     
    def pop(self):
        #TO DO: delete pass and complete method
        if self.__size == 0:    #empty list
            return None
        
        if self.__size == 1:
            temp= self.__head 
            self.__head= None
            self.__tail= None
           
        else:
            temp=self.__tail
            self.__tail =self.__tail.getPrevious()
            self.__tail.setNext(None)
            
        self.__size -= 1
        
        return temp
    
    def sort(self):
        #TO DO: delete pass and complete insertion sort  
        if CardList.getSize(self)==0:
            return None
        elif CardList.getSize(self)==1:
            return str(CardList.getHead(self))
        else:
            
            temp=self.__head
            current=self.__head.getNext()
            after=current.getNext()
            while current!= None:
                while current < temp and current.getNext()!=None:
                    if temp!=self.__head:
                        temp=temp.getPrevious()
                if temp==self.__head and current < temp.getNext():
                    if current > temp and after != None:
                        current.getPrevious().setNext(current.getNext())
                        current.getNext().setPrevious(current.getPrevious())
                        current.setNext(temp.getNext())
                        current.setPrevious(temp)
                        temp.getNext().setPrevious(current)
                        temp.setNext(current)
                        current=after
                        temp=current.getPrevious
                
                
                
            #print(self)
               
      
    def __str__(self):
        #TO DO: delete pass and complete method
        s='|'
        current = self.__head
        while current != self.__tail:
            s= s+ ' '
            s += str(current)
            current=current.getNext()
        s= s + ' ' + str(self.__tail) + ' |'
        return s



class CardStack():
    # DO NOT CHANGE __init__ method
    def __init__(self):
        '''
        Initializes the CardStack, which is essentially a linked Stack.
        Input: N/A
        Returns: None
        '''        
        self.__cards = CardList()  # do not change
        
    def push(self, card):
        #TO DO: delete pass and complete method
        if CardStack.isEmpty(self):
            self.__cards.append(card)
            return True
        elif self.__cards.getTail().getRank() < card.getRank():
            self.__cards.append(card)
            return True
        else:
            return False
    def pop(self):
        #TO DO: delete pass and complete method
        return self.__cards.pop
    
    def peak(self):
        #TO DO: delete pass and complete method
        return self.__cards.getTail() 
    
    def isEmpty(self):
        #TO DO: delete pass and complete method
        if self.__cards.getSize() == 0:
            return True
        else:
            return False

    
    def __str__(self):
        #TO DO: delete pass and complete method
        return str(self.__cards)
    

   
class Table:
    # DO NOT CHANGE __init__ method
    def __init__(self):
        '''
        Initializes the Solitaire table. On the table, we will have 1 deck of cards, 
        1 playing pile, 4 foundation piles, and the 7 columns of cards.
        Input: N/A
        Returns: None
        '''
        NUM_COLUMNS = 7
        self.__deck = CardList()        # do not change
        self.__playingPile = CardList() # do not change
        self.__clubs = CardStack()      # do not change
        self.__hearts = CardStack()     # do not change
        self.__spades = CardStack()     # do not change
        self.__diamonds = CardStack()   # do not change
                
        self.__columns = []
        for col in range(NUM_COLUMNS):
            self.__columns.append(CardList())  # do not change      
     
    # DO NOT CHANGE populateDeck method 
    def populateDeck(self, filename):
        '''
        Adds cards to deck based on information in provided text file. We can assume that if
        we can read from the text file, it contains information for a complete and valid deck.
        Input: filename (str) - name of text file
        Returns: None
        '''
        # Important assumption in this implementation: 
        # the top of the deck is at the tail of our CardList
        
        fin = open(filename, 'r')
        for line in fin:
            cardStr = line.strip()
            self.__deck.add(CardNode(cardStr[0], cardStr[1], False)) 
        fin.close()
    
    def rigGame(self):
        #TO DO: delete pass and complete method
        pass
	
    def dealGame(self):
        #TO DO: delete pass and complete method
        '''
        for cols in range(NUM_COLUMNS):
            for 
    '''
    def drawThree(self):
        #TO DO: delete pass and complete method
        pass            
   
    def playPileToFoundation(self):
        #TO DO: delete pass and complete method
        pass
    
    def columnToFoundation(self, fromIndex):
        #TO DO: delete pass and complete method
        pass
    
    def displayTable(self):
        #TO DO: delete pass and complete method
        pass
        
    def gameWon(self):
        #TO DO: delete pass and complete method
        pass


################################
## Functions to Test classes  ##
################################
def testCardNode():
    
    card1 = CardNode('k', 'c')
    card2=CardNode('4','d')
    print(card1)
    print(card2)
    print(CardNode.__lt__(card1,card2))
    print(CardNode. isPreviousRank(card1,card2))
    
    # write additional tests here
    
def testCardList():
    card1 = CardNode('2', 'h')   
    card2=CardNode('k','c')  
    card3= CardNode('q', 'c')
    card9=CardNode('a','s')
    card4=CardNode('k','d')
    card8=CardNode('6','h')
    
    
    deck = CardList()
   
    
    # write additional tests here
    deck.add(card1)    
    deck.append(card2) 
    deck.append(card3)
    deck.append(card4)
    deck.append(card8)
    deck.append(card9)        
    
    print("unsorted:",deck)
    deck.sort()
    print("sorted:",deck) 
    
def testCardStack():
    stack = CardStack()
    card1 = CardNode('A', 'h')
    print(stack.push(card1))
   
    # write additional tests here
    print(stack.peak())
    print(stack.isEmpty())
    print(stack)    
    
def testTable():
    table = Table()
    # write tests here
    
    
if __name__ == '__main__':
    # comment/uncomment tests as required.  You may add more tests in any format.
    
    testCardNode()
    testCardList()
    testCardStack()
    testTable()
	