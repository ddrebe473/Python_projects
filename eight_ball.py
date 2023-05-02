import random

while True:

    answer = [" It is certain.", "Yes.", "Don't count on it.",
              "No.", "Ask again later.", "Better not tell you now."]

    try:
        put = input("Enter your question: ")
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        if put:
            {
            print(random.choice(answer))
        } 
