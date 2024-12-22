#!/usr/bin/python

# Written by: Romel FG Flores <rom.flores@gmail.com>

import random

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def generate_code():
  code = ["","","",""]
  for item in range(4):
    code[item] = str(random.randrange(1,7))
  return code


def get_correct_count(code, guess):
  correct_ctr = ""
  misplaced_ctr = ""
  stash_code = []
  stash_guess = []

  # get correct
  for item in range(4):
    if code[item] == guess[item]:
      correct_ctr += "O"
    else:
      stash_code.append(code[item])
      stash_guess.append(guess[item])

  # get misplaced
  for item in range(len(stash_code)):
    if stash_guess[item] in stash_code:
      misplaced_ctr += "X"
      stash_code.remove(stash_guess[item])

  return (str(correct_ctr) + str(misplaced_ctr) + "----")[:4]

  # if len(correct_ctr) == 0 and len(misplaced_ctr) == 0:
  #   return "----"
  # else:
  #   return str(correct_ctr) + str(misplaced_ctr)


print("######################################################")
print("#        MASTER MIND!                                #")
print("######################################################")
print("#  Guess the 4 number key combination.               #")
print("#  valid values are 1 to 6                           #")
print("#  Each O means correct value and correct position   #")
print("#  Each X means correct value but incorrect position #")
print("#  type quit, if you're a weakling!                  #")
print("#  You have 15 attempts ... start guessing!          #")        
print("######################################################")
print("# Written by: Romel FG Flores <rom.flores@gmail.com> #")
print("######################################################")
print("---->")

# code = ["1","2","4","4"]
code = generate_code()
# print(code)
hint = ""
counter = 0

while True:
  counter += 1
  guess = None
  
  while not guess:
    guess = input("[" + str(counter) + "] ")
    # print( CURSOR_UP_ONE + ERASE_LINE )  

  if guess == "quit":
    print("the code is " + "".join(code))
    break

  guess = (guess + "    ")[:4]

  hint = get_correct_count(code, guess)
  print( CURSOR_UP_ONE + ERASE_LINE + "[" + str(counter) + "] " + guess + "   " + str(hint) + "\n")
  # print( "[" + str(counter) + "] " + guess + "   " + str(hint) + "\n")
  # print( guess + "   " + str(hint) + "\n")

  if hint.strip() == "OOOO":
    print("You Win!")
    break

  if counter == 15:
    print("You Failed!")
    print("the code is " + "".join(code))
    break

