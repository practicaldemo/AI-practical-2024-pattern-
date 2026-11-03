import re

def chatbot_response(user_input):
    user_input = user_input.lower()
    rules = {
        r'.* hello .*|.* hi .*': "Hello! How can I help you today?",
        r'.* how are you .*': "I'm just a script, but I'm doing well!",
        r'.* name .*': "I am a simple rule-based AI chatbot.",
        r'.* bye .*': "Goodbye! Have a great day ahead!",
    }
    
    for pattern, response in rules.items():
        if re.match(pattern, user_input):
            return response
            
    return "I'm sorry, I don't understand that."

# Simulated conversation
messages = ["Hi", "What is your name?", "How are you?", "Bye"]

for msg in messages:
    print(f"You: {msg}")
    print(f"Bot: {chatbot_response(msg)}")
    