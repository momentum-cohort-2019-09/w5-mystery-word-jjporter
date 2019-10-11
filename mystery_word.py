import random

with open('words.txt') as file:
  content = file.read().lower()

  words = content.split()

  random_word = random.choice(words)

#set difficulty
def set_difficulty():
  difficulty = input('Select difficulty - easy, medium, or hard: ').lower()
  if difficulty == 'easy':
    return difficulty
  elif difficulty == 'medium':
    return difficulty
  elif difficulty == 'hard':
    return difficulty
  else:
    return set_difficulty()

#difficulty parameters
def get_word(difficulty):
  random_word = ""
  with open('words.txt') as file:
    content = file.read().lower()
    words = content.split()
    random_word = random.choice(words)
  if difficulty == 'easy':
    if len(random_word) <= 5:
      return random_word
    else:
      return get_word(difficulty)
  elif difficulty == 'medium':
    if 6 <= len(random_word) <= 8:
      return random_word
    else:
      return get_word(difficulty)
  elif difficulty == 'hard':
    if len(random_word) > 9:
      return random_word
    else:
      return get_word(difficulty)


#function to loop through random word until all letters are guessed
def game_play(random_word):
  difficulty = set_difficulty()
  random_word = get_word(difficulty)
  blanks = ["_"] * len(random_word)
  wrong_letters = []
  guesses = 0
  game_over = False
  print(" ".join(blanks))
  while game_over == False:
    guesses_left = 8 - guesses
    print(f"You have {guesses_left} guesses left...")
    user_guess = input('Guess a letter! ')
    print(user_guess)
    if len(user_guess) != 1:
      print(f"Guess only 1 letter.")
    if user_guess in random_word:
      print('Correct')
      for index in range(len(random_word)):
        if user_guess == random_word[index]:
          blanks[index] = user_guess
      print(" ".join(blanks))
      if ("".join(blanks)) == random_word:
        game_over = True
        print(f"You guessed it! The word was {random_word}. It took you {guesses} guess(es).")
      elif guesses == 8:
        game_over = True
        print(f"You lose. The word was {random_word}")
    else:
      print('Nope')
      if user_guess in wrong_letters:
        print(f"You already guessed that letter. Guess again.")
      wrong_letters.append(user_guess)
      print(wrong_letters)
      guesses += 1

game_play(random_word)





