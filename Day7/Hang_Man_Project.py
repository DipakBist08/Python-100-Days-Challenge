import random
word_list = ["ardvark","baboon","camel"]

choosen_word = random.choice(word_list)
user_input = input("Guess a letter:  ").lower()

for letter in choosen_word:
    if letter == user_input:
        print("Correct.")
    else:
        print("Wrong!!")

