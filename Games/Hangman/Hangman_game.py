import random
import hangman_stages
print("Lets play Hangman!!")
print("You have only 6 lives so try to guess the word within 6 attempts! GOOD LUCK!!")
words=["apple","mango","orange","cashew","grapes","honey"]
lives=6
chosen_word=random.choice(words)
# print(chosen_word)
display=[]
for i in range(len(chosen_word)):
    display+='_'
print(display)
game_over=False
while not game_over:
    guess=input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=guess
    print(display)
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You lose!!")
    if '_' not in display:
        game_over=True
        print("You win!!")
    print(hangman_stages.stages[lives])