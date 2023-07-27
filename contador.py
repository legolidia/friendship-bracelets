from letters import letters
from phrases import phrases
from lettersused import lettersAlreadyChecked

def countLetters(phrase, lettersAlreadyChecked):
  initialPhrase = phrase.upper().replace(" ", "")
  print(phrase)
  print(initialPhrase)

  lettersAlreadyChecked = dict.fromkeys(lettersAlreadyChecked, 0)
  letter_verified = []
  notEnough = []

  for letter in initialPhrase:
    lettersAlreadyChecked[letter] += 1

  for letter in initialPhrase:
    if letter not in letter_verified:
      letter_verified.append(letter)
      if lettersAlreadyChecked[letter] > letters[letter]:
        print("not enough %s's" % letter)
        notEnough.append(letter)
      else:
        print("enough %s's" % letter)

  print("letters not enough:", notEnough)

  if notEnough == []:
    print("You have enough letters to make the phrase: %s" % phrase)
  else:
    print("You don't have enough letters to make the phrase: %s" % phrase)

for phrase in phrases:
  countLetters(phrase, lettersAlreadyChecked)
  pause = input("Press enter to continue...")
