import random
import hangman_art,getAWord
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def startGame():
    diaplay = list()
    chosenWord=str(getAWord.get_a_word()).replace('[\'','').replace('\\','').replace('\']','')
    chosenWord.replace('\'','')
    chosenWordLenght=len(chosenWord)


    for wordCount in range(chosenWordLenght):
        diaplay+='_'

    print(diaplay)
    return diaplay,chosenWordLenght,chosenWord

lives = 6
endOfGame=False
display,chosenWordLenght,chosenWord = startGame()
usedletters=list()
while not endOfGame:
    print('Used letters: '+ str(usedletters))
    guess = input('Guess a letter: ').lower()#harfileri küçültüyoruz
    clear()
    if guess in display:
        print(f'You have already guessed {guess}')
    for position in range(chosenWordLenght):
        if chosenWord[position]==guess:
            display[position]=guess
    if guess not in chosenWord:
        print(f'You guessed {guess}, that is not in the word. You lose a life.')
        usedletters.append(guess)
        lives -=1
        if lives==0:
            endOfGame=True
            print(f'you lose. Word is {chosenWord}')
            replay=input('Do you want to replay? (y/other letter):').lower()
            if(replay=='y'):
                lives=6
                clear()
                endOfGame=False
                display.clear()
                usedletters.clear()
                display,chosenWordLenght,chosenWord = startGame()
                continue

    print(display)

    if '_' not in display:
        endOfGame=True
        print('You win!')
        replay = input('Do you want to replay? (y/other letter):').lower()
        if (replay == 'y'):
            lives = 6
            clear()
            endOfGame = False
            display.clear()
            display, chosenWordLenght, chosenWord = startGame()
            continue

    print(hangman_art.stages[lives])