from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Create a new chat bot named Charlie
chatbot = ChatBot('JobOpenings')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
print("Type something to begin...")

while True:
    try:
        user_input = input()
        response = chatbot.get_response(user_input)
        print(response)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
