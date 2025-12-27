def simple_chatbot():
    print(" Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")
    
    # 1. Loop to keep the conversation going
    while True:
        # 2. Get user input and convert to lowercase for case-insensitivity
        user_input = input("You: ").lower().strip()
        
        # 3. Rule-based logic using If-Elif-Else
        if user_input == "hello" or user_input == "hi":
            print(" Chatbot: Hi there! How can I help you today?")
            
        elif user_input == "how are you":
            print(" Chatbot: I'm just a computer program, but I'm running perfectly! Thanks for asking.")
            
        elif "name" in user_input:
            print(" Chatbot: I am a text-based chatbot created for CodeAlpha.")
            
        elif user_input == "bye" or user_input == "quit":
            print(" Chatbot: Goodbye! Have a great day! 👋")
            break # Exit the loop
            
        else:
            # Default response for unknown inputs
            print("🤖 Chatbot: I'm sorry, I don't understand that. Try saying 'hello' or 'how are you'.")

# Run the function
if __name__ == "__main__":
    simple_chatbot()
