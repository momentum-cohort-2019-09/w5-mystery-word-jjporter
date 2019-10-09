import random

with open('words.txt') as file:
  content = file.read()

lowercase = content.lower()

words = content.split()

random_word = random.choice(words)

#function to loop through random word until all letters are guessed
def game_play(random_word):
  blanks = ["_"] * len(random_word)
  print(blanks)
  wrong_letters = []
  guesses = 0
  game_over = False
  while game_over == False:
    print(random_word)
    user_guess = input('Guess a letter! ')
    print(user_guess)
    if user_guess in random_word:
      print('Correct')
      for index in range(len(random_word)):
        if user_guess == random_word[index]:
          blanks[index] = user_guess
      print(blanks)
      s = ""
      if (s.join(blanks)) == random_word:
        game_over = True
    else:
      print('Nope')
      wrong_letters.append(user_guess)
      print(wrong_letters)
    guesses += 1
  print(f"You guessed it! The word was {random_word}. It took you {guesses} guess(es).")

game_play(random_word)




