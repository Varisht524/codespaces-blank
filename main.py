def chatbot():
    print("Welcome to the chatbot! ")

    # Collect user information
    name = input("What's your name? ")
    age = input("How old are you? ")

    print(f"Nice to meet you, {name}! You are {age} years old.")
    
    # Ask how it can help
    print("How can I help you today?")
    
    while True:
        # Menu options
        print("\nPlease choose an option:")
        print("1. Ask a question ")
        print("2. Get some information ")
        print("3. Exit the conversation")
        
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            print("You chose to ask a question. ")
        elif choice == "2":
            print("You chose to get some information. ")
        elif choice == "3":
            print(f"Goodbye, {name}! Thanks for chatting. ")
            break
        else:
            print("Invalid choice. Please try again.")


chatbot()








