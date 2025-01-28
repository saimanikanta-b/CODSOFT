def chatbot():
    print("Chatbot: Hi! I'm your chatbot. How can I help you today?")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hello! How can I assist you?")
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm just a Chatbot, so I don't have feelings, but I'm here to help!")
        elif "your name" in user_input:
            print("Chatbot: I'm a simple chatbot created to help you. You can call me Bot!")
        elif "how old are you" in user_input:
            print("Chatbot: I don't have an age. I'm just a program designed to assist you.")
        elif user_input in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you rephrase?")
chatbot()