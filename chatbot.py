#easy chatbot - made by python

print("Bot: Hello! I am a chatbot. How are you?")

user_name = ""  # To store user's name
waiting_for_name = False  # To track if bot is waiting for user's name

while True:
    user_input = input("You: ").strip()
    lower_input = user_input.lower()

    if waiting_for_name:
        user_name = user_input.capitalize()
        print(f"Bot: Nice to meet you, {user_name}!")
        waiting_for_name = False

    elif "your name" in lower_input:
        print("Bot: My name is Pybot, what's your name?")
        waiting_for_name = True

    elif "good" in lower_input or "fine" in lower_input:
        print("Bot: Glad to hear that!")

    elif "and you" in lower_input:
        print("Bot: I am also fine too. What do you do?")

    elif "i am talking to you" in lower_input:
        print("Bot: How sweet!")

    elif "thank you" in lower_input:
        print("Bot: Welcome!")

    elif "what do you do" in lower_input:
        print("Bot: I talk to you.")

    elif "bye" in lower_input:
        if user_name:
            print(f"Bot: Goodbye, {user_name}! See you again.")
        else:
            print("Bot: Goodbye! See you again.")
        break

    else:
        print("Bot: Sorry, I didn't understand. Could you say that again?")