secret_word = "Sheik Hasina"
guess = ""
guess_limit = 5
guess_count = 0
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter you guess: ")
        guess_count+=1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You're out of guesses. YOU LOST!")
else:
    print("Correct Guess. YOU WON!")

