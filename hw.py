skaicius = 8

guess = int(input("First guess. Guess the number:"))

if guess == skaicius:
    print("Congratulations")
else:
    guess = int(input("Second guess:"))

    if guess == skaicius:
        print("Congratulations")
    else:
        guess = int(input("Third guess:"))

        if guess == skaicius:
            print("Congratulations")
        else:
            guess = int(input("You lost"))