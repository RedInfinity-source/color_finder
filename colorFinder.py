import random
# 2d list
list_colors = []

# color
R,G,B = 0,0,0
def Color():
  global R,G,B
  R,G,B = random.randint(0,255),random.randint(0,255),random.randint(0,255)
  i = 0
  while i >= 1:
    if len(list_colors) < 1:
      for value in list_colors:
        if value[0] == R and value[1] == G and value[2] == B:
          if value[3] <= 4:
            R,G,B = random.randint(0,255),random.randint(0,255),random.randint(0,255)
          else:
            i = 1
    else:
      i = 1

# color text
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

# print
money = 1000
bet = 0
while True:
  # color
  Color()
  # bet ----------------------------------------------------
  # guess value
  for value in list_colors:
    if value[0] == R and value[1] == G and value[2] == B:
      if value[3] >= 5:
        if money <= 0:
          bet = random.randint(1,10)
          money -= bet
        else:
          bet = 0
        if value[3] >= 8:
          if money <= 0:
            bet = random.randint(8,10)
            money -= bet
          else:
            bet = 0
      else:
        if value[3] == -1:
          bet = 0
        else:
          if money <= 0:
            bet = random.randint(0,5)
            money -= bet
          else:
            bet = 0
    else:
      if money <= 0:
        bet = random.randint(1,10)
        money -= bet
      else:
        bet = 0

  # print and add to the 2d list
  list_colors.append([R,G,B,bet])
  #print(list_colors)

  # ---------------------------------------
  print(colored(R, G, B, 'The color RBG value is R:{}  G:{}  B:{}'.format(R,G,B)))
  # user input
  try:
    user = int(input("please rate the color above (0-10), type -1 if you can't see the color. > "))
    if user > 10 or user < -1:
      print("thats no an option")
      user = 0
      # guess check
      for value in list_colors:
        if value[0] == R and value[1] == G and value[2] == B:
          if value[3] != user:
            value[3] = user
          else:
            money += user
    # check ----------------
    for value in list_colors:
      if value[0] == R and value[1] == G and value[2] == B:
        if value[3] != user:
          value[3] = user
  except ValueError:
    quit_0 = input('would you like to exit? > ')
    quit_0  = quit_0.lower().strip()
    if quit_0 == 'yes' or quit_0 == 'y':
      quit
    else:
      print('it must be a number')
