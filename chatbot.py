import random

responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thanks!", "I'm good, how about you?", "All systems go!"],
    "what's your name": ["I'm just a chatbot.", "You can call me coco .", "I go by quantumaniacs"],
    "bye": ["Goodbye!", "See you later!", "Bye now!"]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I'm not sure how to respond to that."

if __name__ == "__main__":
    print("Chatbot: Hi! I'm your friendly chatbot. How can I assist you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")
