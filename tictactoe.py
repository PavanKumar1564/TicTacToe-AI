import random

class Player():
  def __init__(self,letter):
    self.letter=letter

  def getmove(self,game):
    pass

class user(Player):
  def __init__(self,letter):
    super().__init__(letter)

  def getmove(self,game):
    notanumber=True
    val="None"
    while notanumber and len(game.available_moves())!=0 and game.iswinner()=="np":
      try:
        val=int(input("enter the square value"))
        if val in game.available_moves() and 0<val<10:
          notanumber=False
      except:
        print("tryagain")

    return val

class Computer(Player):
  def __init__(self,letter):
    super().__init__(letter)

  def getmove(self,game):
    return random.choice(game.available_moves())



class SmartComputer(Player):
  def __init__(self,letter):
    super().__init__(letter)

  def getmove(self,game):
    val="none"
    if len(game.available_moves()) == 9:
      val=random.choice(game.available_moves())
    else:
      #score=[]
      val=self.abc(game,letter)

    return val


  def abc(self,game,letter):
    d=dict()
    c=0
    for move in game.available_moves():
      game.update_board_2(move,self.letter) 
      score=self.minimax(game,"o")
      #game.print_board()
      game.update_board_2(move," ")
      
      d[move]=score
    #print("@@@@@@@@@@@@@@@@@")
    return self.keywithmaxval(d)

  def keywithmaxval(self,d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]



  def minimax(self,game,letter):
    #print(c)
    if game.iswinner()=="np" and game.no_empty_space()==0:
      #print(game.no_empty_space())
      return 0
    elif game.iswinner()=="x":
      return 1
    elif game.iswinner()=="o":
      return -1

    score=[]
    #print(game.available_moves())
    if letter=="x":
      for move in game.available_moves():
        game.update_board_2(move,letter)
        score.append(self.minimax(game,"o"))
        game.update_board_2(move," ")
        #game.print_board()
      best_score=max(score)


    elif letter=="o":
      for move in game.available_moves():
        game.update_board_2(move,letter)
        score.append(self.minimax(game,"x"))
        game.update_board_2(move," ")
        #game.print_board()
      best_score=min(score)

    #game.print_board()
    return best_score



class TTT():
  def __init__(self):
    self.board=[" "]*9

  @staticmethod
  def print_board_static():
    num_board=[str(i) for i in range(1,10)]
    for row in [num_board[i*3:(i+1) * 3] for i in range(3)]:
      print('| ' + ' | '.join(row) + ' |')
    print("_______________________")


  def update_board(self,square,letter):
    if square in game.available_moves():
      self.board[square-1]=letter
      self.print_board()

  def update_board_2(self,square,letter):
    #if square in game.available_moves():
    self.board[square-1]=letter

  def available_moves(self):
    # k=[i+1 for i, x in enumerate(self.board) if x == " "]
    # print(k)
    return [i+1 for i, x in enumerate(self.board) if x == " "]

  def print_board(self):
    #self.board=[str(i) for i in range(1,10)]
    for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
      print('| ' + ' | '.join(row) + ' |')
    print("_______________________")

  def iswinner(self):
    for i in range(0,3):
      if self.board[i*3:(i+1)*3].count("x")==3:
        return "x"
      elif self.board[i*3:(i+1)*3].count("o")==3:
        return "o"

    for i in [0,1,2]:
      if self.board[i:9:3].count("x")==3:
        return "x"
      elif self.board[i:9:3].count("o")==3:
        return "o"

    daigonal1=[self.board[i] for i in [0,4,8]]
    daigonal2=[self.board[i] for i in [2,4,6]]

    if daigonal1.count("x")==3:
      return "x"
    elif daigonal1.count("o")==3:
      return "o"

    if daigonal2.count("x")==3:
      return "x"
    elif daigonal2.count("o")==3:
      return "o"

    return "np"

  def no_empty_space(self):
    return self.board.count(" ")


def play(game,x_player,o_player,letter):
  while game.iswinner() == "np" and game.no_empty_space():
    if letter == "x" and game.iswinner() == "np":
      square=x_player.getmove(game)
      print(square)
      game.update_board(square,letter)
      letter="o"
      #play(game,x_player,o_player,letter,end_game)

    if letter == "o" and game.iswinner() == "np":
      square=o_player.getmove(game)
      print(square)
      game.update_board(square,letter)
      letter="x"
      #play(game,x_player,o_player,letter,end_game)

  return


x_player=SmartComputer("x")
o_player=user("o")
game=TTT()
letter="x"

game.print_board_static()
play(game,x_player,o_player,letter)


if game.iswinner()=="np":
  print("tie")
else:
  print(game.iswinner())


