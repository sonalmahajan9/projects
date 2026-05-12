def chatbot():
    print("Chatbot: Hello! I am your assistant.")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user in ["hello", "hi", "hey"]:
            print("Bot: Hello! How can I help you?")
        
        elif "name" in user:
            print("Bot: I am a simple chatbot created for AI practical.")
        
        elif "your creator" in user or "who made you" in user:
            print("Bot: I was created by a computer engineering student")
        
        elif "how are you" in user:
            print("Bot: I am fine! How about you?")
        
        elif "i am fine" in user or "good" in user:
            print("Bot: Glad to hear that!")
        
        elif "course" in user:
            print("Bot: This is Artificial Intelligence Lab.")
        
        elif "college" in user:
            print("Bot: PCCOER, Ravet Pune.")
        
        elif "location" in user or "where" in user:
            print("Bot: I exist inside your computer system")
        
        elif "time" in user:
            import datetime
            print("Bot: Current time is", datetime.datetime.now().strftime("%H:%M:%S"))
        
        elif "date" in user:
            import datetime
            print("Bot: Today's date is", datetime.datetime.now().date())
        
        elif "day" in user:
            import datetime
            print("Bot: Today is", datetime.datetime.now().strftime("%A"))
        
        elif "weather" in user:
            print("Bot: I can't check live weather yet, but it's always coding weather")
        
        elif "help" in user:
            print("Bot: You can ask me about time, date, college, course, or greetings.")
        
        elif "hobby" in user:
            print("Bot: I like chatting with humans and learning new things!")
        
        elif "joke" in user:
            print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")
        
        elif "thanks" in user or "thank you" in user:
            print("Bot: You're welcome!")
        
        elif "python" in user:
            print("Bot: Python is a powerful and easy-to-learn programming language.")
        
        elif "ai" in user:
            print("Bot: AI stands for Artificial Intelligence, making machines smart.")
        
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day")
            break
        
        else:
            print("Bot: Sorry, I don't understand that.")
chatbot()