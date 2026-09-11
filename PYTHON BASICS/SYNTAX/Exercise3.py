import random

error_phrases = [
    "Oops buddy, with that luck you better not buy a lottery ticket.",
    "Try again, you almost hit... the neighbor!",
    "Almost, but no. That guess was colder than yesterday's coffee.",
    "You didn't even hit the post! Try again, champ.",
    "That was way off... Well, it could be worse, but don’t push it 😅."
]

winning_phrase = "Yesss! Your winning brain cell finally kicked in."

play_again = "y"
while play_again.lower() == "y":
    print("🎮 Welcome to the Secret Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    
    secret_number = random.randint(1, 10)
    guess = 0
    attempts = 0

    while guess != secret_number:
        try:
            guess = int(input("Enter your number: "))
            attempts += 1
            if guess != secret_number:
                print(random.choice(error_phrases))
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempt(s).")
        except ValueError:
            print("Please enter a valid number... no letters or hieroglyphs.")
            