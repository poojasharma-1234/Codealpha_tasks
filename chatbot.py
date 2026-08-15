def chatbot():
    print("chatbot:hello! how can i help you?")
    while True:
        user_input = input("you:").lower()
        if user_input == "hello":
            print("chatbot: hi!")
        elif user_input == "how are you":
            print("chatbot: I'm fine, tanks!")
        elif user_input == "bye":
            print("chatbot: goodbye!")
            break
        else:
            print("chatbot: sorry, I don't understand.")
chatbot()