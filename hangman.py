import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
word_len= len(chosen_word)
for position in range(word_len):
    placeholder += "_"
print(placeholder)
guess = input("guess a letter?")
guess.lower()
display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)     