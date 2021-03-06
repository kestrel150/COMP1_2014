# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014


import random
import datetime
import pickle

NO_OF_RECENT_SCORES = 10
ACE_HIGH = False
SAME_FAIL = True


class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0


class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.Date = ''

Deck = [None]
RecentScores = [None]
Choice = ''


def GetRank(RankNo):
  Rank = ''
  if RankNo == 1:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  elif RankNo == 14:
    Rank = "Ace"
  return Rank


def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit


def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Save scores')
  print('6. Options')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')


def GetMenuChoice():
  Choice = input()
  Choice = Choice[0].lower()
  print()
  return Choice


def DisplayOptions():
  print()
  print("OPTION MENU")
  print()
  print("1. Set Ace to be High or Low: ")
  print("2. Set same card to end game or not: ")
  print()

  
def GetOptionChoice():
  OptionChoice = input("Select an option from the menu (or enter q to quit to the main menu): ")
  print()
  return OptionChoice


def SetOptions():
  DisplayOptions()
  OptionChoice = GetOptionChoice()
  if OptionChoice == '1':
    SetAceHighOrLow()
  if OptionChoice == '2':
    SetSameScore()
  if OptionChoice == 'q':
    print("Returning to the menu...")
    print()


def SetAceHighOrLow():
  global ACE_HIGH
  AceOption = input("Do you want the ace to be (h)igh or (l)ow: ")
  if AceOption == "h":
    ACE_HIGH = True
  elif AceOption == "l":
    ACE_HIGH = False


def SetSameScore():
  global SAME_FAIL
  SameOption = input("Do you want the game to end when the next card is the same as the previous one? (y|n) ")
  if SameOption == "y":
    SAME_FAIL = True
  elif SameOption == "n":
    SAME_FAIL = False
    
  
def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    if Deck[Count].Rank == 1 and ACE_HIGH == True:
      Deck[Count].Rank = 14
    Count = Count + 1

 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit


def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()


def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0


def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True

  return Higher


def GetPlayerName():
  print()
  ValidName = False
  while ValidName == False:
    PlayerName = input('Please enter your name: ')
    print()
    ValidName = PlayerName.isalpha()
    if len(PlayerName) not in range(2,16):
      ValidName = False
    if ValidName == False:
      print("Please enter a valid name (Only characters from the alphabet are allowed, and the name must be from 2 characters to 15 characters long)")

  return PlayerName


def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
  Choice = Choice[0].lower()
  return Choice


def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()


def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()


def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    RecentScores[Count].Date = ""


def DisplayRecentScores(RecentScores):
  BubbleSortScores(RecentScores)
  print()
  print('Recent Scores: ')
  print()
  print("{0:<15}{1:<9}{2:<10}".format("Name","Score","Date"))
  print()
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print("{0:<15}{1:<9}{2:<10}".format(RecentScores[Count].Name, RecentScores[Count].Score, RecentScores[Count].Date))
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()


def UpdateRecentScores(RecentScores, Score):
  PlayerName = GetPlayerName()
  RawTime = datetime.date.today()
  CurrentTime = datetime.date.strftime(RawTime, "%d/%m/%y")
  FoundSpace = False
  Count = 1
  while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
    if RecentScores[Count].Name == '':
      FoundSpace = True
    else:
      Count = Count + 1
  if not FoundSpace:
    for Count in range(1, NO_OF_RECENT_SCORES):
      RecentScores[Count].Name = RecentScores[Count + 1].Name
      RecentScores[Count].Score = RecentScores[Count + 1].Score
      RecentScores[Count].Date = RecentScores[Count + 1].Date
    Count = NO_OF_RECENT_SCORES
  RecentScores[Count].Name = PlayerName
  RecentScores[Count].Score = Score
  RecentScores[Count].Date = CurrentTime


def SaveScores(RecentScores):
  with open("save_scores.txt",mode ="w",encoding="utf-8") as score_file:
    for Count in range(1, NO_OF_RECENT_SCORES+1):
      print("Saving score {0}...".format(str(Count)))
      
      score = str(RecentScores[Count].Score)
      
      score_file.write(RecentScores[Count].Name+("\n"))
      score_file.write(score+("\n"))
      score_file.write(RecentScores[Count].Date+("\n"))
      
  print("Save Complete!")


def SaveGame(NextCard,LastCard,Deck,NoOfCardsTurnedOver,Score):
  with open("SavedGame.dat", mode="wb") as SavedGame:
    GameAttributes = [NextCard,LastCard,Deck,NoOfCardsTurnedOver,Score]
    pickle.dump(GameAttributes,SavedGame)
  with open("deck.txt",mode="w",encoding="utf-8")as SavedDeck:
    for count in Deck:
      if count != None:
        SavedDeck.write(str(count.Suit)+"\n")
        SavedDeck.write(str(count.Rank)+"\n")

def PlayGame(Deck, RecentScores):
  Score = 0
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n') and (Choice != 's'):
      Choice = GetChoiceFromUser()
    if Choice in ["y","n"]:
      DisplayCard(NextCard)
      NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
      Higher = IsNextCardHigher(LastCard, NextCard)
      if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
        Score = Score + 1
        DisplayCorrectGuessMessage(Score)
        LastCard.Rank = NextCard.Rank
        LastCard.Suit = NextCard.Suit
      elif (not Higher and SAME_FAIL == False) and (LastCard.Rank == NextCard.Rank):
        print("The next card is the same rank. You do not fail but gain no extra point.")
        print()
      else:
        GameOver = True
    elif Choice == 's':
      SaveGame(NextCard,LastCard,Deck,NoOfCardsTurnedOver,Score)
      GameOver = True
  if GameOver and Choice != 's':
    DisplayEndOfGameMessage(Score)
    ValidHighScoreChoice = False
    while ValidHighScoreChoice == False:
      Addscore = input("Do you want to add your score to the high score table? (Y or N): ")
      Addscore = Addscore[0].upper()
      if Addscore == "Y" or Addscore == "N":
        ValidHighScoreChoice = True
    if Addscore == "Y":
      UpdateRecentScores(RecentScores, Score)
  elif Choice != 's':
    DisplayEndOfGameMessage(Score)
    UpdateRecentScores(RecentScores, Score)
  else:
    print("Game has been saved, you may return to the game later.")
    print()


def BubbleSortScores(RecentScores):
  sort = False
  while not sort:
    sort = True
    for Count in range(1,NO_OF_RECENT_SCORES):
      if RecentScores[Count].Score < RecentScores[Count + 1].Score:
        sort = False
        temp = RecentScores[Count + 1]
        RecentScores[Count+1] = RecentScores[Count]
        RecentScores[Count] = temp


def LoadScores():
  RawScoresList = []
  
  with open("save_scores.txt",mode="r",encoding="utf-8") as score_file:
    for Count in range(1, NO_OF_RECENT_SCORES + 1):
      Name = score_file.readline()
      Score = score_file.readline()
      Date = score_file.readline()

      Name = Name.rstrip("\n")
      Score = Score.rstrip("\n")
      Date = Date.rstrip("\n")

      Score = int(Score)

      RecentScores[Count].Name = Name
      RecentScores[Count].Score = Score
      RecentScores[Count].Date = Date

def LoadSaveGame
    
if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = ''
  try:
    LoadScores()
  except IOError:
    print("Save file not found, a blank save file shall be created.")
    print()
    SaveScores(RecentScores)
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      SaveScores(RecentScores)
    elif Choice == '6':
      SetOptions()
