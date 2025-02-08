import random

Generate_number = random.randint(0,500)
//print(Generate_number)
while True:

    try:
        number = int(input("Enter the number between 0 to 500 that I guessed: "))

        if(number > Generate_number + 50):
            print("You guessed too high.")

        elif(number < Generate_number - 50):
            print("You guessed too low.")

        elif(number > Generate_number):
            print("You guessed high.")

        elif(number < Generate_number):
            print("You guessed low.")
        else:
            print(f"Yes! You guessed the right answer. The number is {Generate_number}")
            break
    except ValueError:
        print("Please enter a valid number.")