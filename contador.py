from letters import letters
from phrases import phrases

def countAlphabetLettersInPhrase(phrase):
    initialPhrase = phrase
    numLetter = 0
    lettersAlreadyChecked = []
    notEnough = []
    for letter in letters:
      for i in phrase:
        if i == letter and letter not in lettersAlreadyChecked:
          phrase = phrase.replace(i, "")
          if i in phrase:
            numLetter += 1
          if numLetter >= letters[letter]:
            print("not enough %s's" % letter)
            notEnough.append(letter)
          else:
            print("enough %s's" % letter)
          lettersAlreadyChecked.append(letter)
      numLetter = 0
    print("letters not enough:", notEnough)
    if notEnough == []:
      print("You have enough letters to make the phrase: %s" % initialPhrase)
    else:
      print("You don't have enough letters to make the phrase: %s" % initialPhrase)

for phrase in phrases:
  phrase = phrase.upper()
  
  for i in phrase:
    if i == " ":
      phrase = phrase.replace(i, "")

    countAlphabetLettersInPhrase(phrase)
  pause = input("Press enter to continue...")
  


        
