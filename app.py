import datetime
import random


jokes = [
    "Why don't programmers like nature? It has too many bugs.",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do Java developers wear glasses? Because they don't C#."
]

quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Believe in yourself and all that you are.",
    "Every day is a new opportunity to learn."
]

facts = [
    "Python was created by Guido van Rossum in 1991.",
    "The first computer bug was an actual moth.",
    "A byte consists of 8 bits.",
    "Artificial Intelligence is a branch of Computer Science."
]


name = input("Enter your name: ")


hour = datetime.datetime.now().hour

if hour < 12:
    greeting = "Good Morning"
elif hour < 18:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

print(f"\n{greeting}, {name}!")
print("I am RuleBot.")
print("Type 'help' for commands.")
print("Type 'exit' to quit.\n")

chat_history = []
query_count = 0

while True:

    user_input = input(f"{name}: ").lower().strip()

    query_count += 1
    chat_history.append(f"{name}: {user_input}")

    
    if user_input in ["hi", "hello", "hey"]:
        response = "Hello! How can I help you today?"

    
    elif "your name" in user_input:
        response = "My name is RuleBot."

    elif "my name" in user_input:
        response = f"Your name is {name}."

    
    elif "age" in user_input:
        response = "I don't have an age. I am a computer program."

    
    elif "sad" in user_input:
        response = "Don't worry. Every challenge is an opportunity to grow."

    elif "happy" in user_input:
        response = "That's wonderful! Keep smiling."

    elif "angry" in user_input:
        response = "Try taking a short break and relaxing."

    
    elif "date" in user_input:
        response = f"Today's date is {datetime.date.today()}"

    elif "time" in user_input:
        response = f"Current time is {datetime.datetime.now().strftime('%H:%M:%S')}"

    
    elif "joke" in user_input:
        response = random.choice(jokes)

    
    elif "quote" in user_input or "motivate" in user_input:
        response = random.choice(quotes)

    
    elif "fact" in user_input:
        response = random.choice(facts)

    
    elif "favorite color" in user_input:
        response = "As a chatbot, I like all colors equally."

    
    elif "weather" in user_input:
        response = "I cannot access live weather data, but I hope it's a pleasant day."

    
    elif "thank you" in user_input or "thanks" in user_input:
        response = "You're welcome! Happy to help."

    
    elif user_input.startswith("calculate"):
        try:
            expression = user_input.replace("calculate", "")
            response = f"Result = {eval(expression)}"
        except:
            response = "Invalid calculation."

    
    elif "queries" in user_input:
        response = f"You have asked {query_count} questions."

    
    elif "history" in user_input:
        print("\n----- CHAT HISTORY -----")
        for msg in chat_history:
            print(msg)
        print("------------------------")
        continue

    
    elif user_input == "help":
        response = """
Available Commands:
- hi / hello
- how are you
- your name
- my name
- age
- date
- time
- joke
- quote
- fact
- weather
- happy / sad / angry
- favorite color
- calculate 10+5
- history
- queries
- thanks
- exit
"""

    
    elif user_input in ["bye", "exit", "quit"]:

        # Save history to file
        with open("chat_history.txt", "w") as file:
            for msg in chat_history:
                file.write(msg + "\n")

        print("Bot: Chat history saved to chat_history.txt")
        print(f"Bot: Goodbye {name}!")
        break

    else:
        response = "Sorry, I don't understand that."

    print("Bot:", response)
    chat_history.append("Bot: " + response)