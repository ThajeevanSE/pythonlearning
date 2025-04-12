import random


lives=6
word_list = ["python", "java", "kotlin", "javascript", "hangman", "programming", "computer", "science"]
chosen_word = random.choice(word_list)
display=[]
for i in range(len(chosen_word)):
    display+= "_" 
game_over=False
while not game_over:
    guessed_letter=input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=letter
    print(display)
    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
           game_over=True
           print("You lose.")
    if '_' not in display:
        game_over=True
        print("You win.")