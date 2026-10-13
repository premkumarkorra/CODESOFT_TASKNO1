import re


class SimpleChatbot:
    """A basic chatbot that responds to messages using predefined rules."""

    exit_commands = {"bye", "goodbye", "exit", "quit"}

    @staticmethod
    def normalize(message):
        return re.sub(r"[^\w\s]", "", message.casefold()).strip()

    def get_response(self, message):
        normalized_message = self.normalize(message)

        if not normalized_message:
            return "Please type a message."
        elif re.search(r"\bhow are you\b", normalized_message):
            return "I'm doing well, thanks for asking! How are you?"
        elif re.search(r"\b(?:good morning|good afternoon|good evening)\b", normalized_message):
            return "Hello! I hope you're having a good day."
        elif re.search(r"\bwhat is up\b|\bwhats up\b", normalized_message):
            return "Not much! I'm here and ready to chat."
        elif re.search(
            r"\bwhat is your name\b|\bwhats your name\b|\bwho are you\b",
            normalized_message,
        ):
            return "I'm a simple rule-based chatbot."
        elif re.search(r"\bwho made you\b|\bwho created you\b", normalized_message):
            return "I was created as a simple chatbot demonstration."
        elif re.search(r"\bhow old are you\b|\byour age\b", normalized_message):
            return "I don't have an age, but I'm always ready to chat!"
        elif re.search(r"\bwhere are you from\b|\bwhere do you live\b", normalized_message):
            return "I live in this program, so I don't have a physical home."
        elif re.search(r"\bcan you hear me\b|\bcan you see me\b", normalized_message):
            return "I can only read the text you type here."
        elif re.search(r"\bcan you remember me\b|\bdo you remember me\b", normalized_message):
            return "I can respond to this conversation, but I don't know you personally."
        elif re.search(r"\b(?:favorite|favourite) color\b", normalized_message):
            return "I like blue. What's your favorite color?"
        elif re.search(r"\b(?:favorite|favourite) food\b", normalized_message):
            return "I don't eat, but pizza is a popular favorite!"
        elif re.search(r"\b(?:favorite|favourite) animal\b", normalized_message):
            return "I think dogs are wonderful. What's your favorite animal?"
        elif re.search(r"\b(?:favorite|favourite) music\b|\bwhat music do you like\b", normalized_message):
            return "I don't listen to music, but I can talk about different kinds!"
        elif re.search(r"\bdo you have a pet\b|\bdo you like animals\b", normalized_message):
            return "I don't have pets, but animals are fun to talk about."
        elif re.search(r"\bdo you like\b", normalized_message):
            return "I don't have feelings or personal preferences, but I'm happy to chat about it."
        elif re.search(r"\btell me a joke\b|\bmake me laugh\b", normalized_message):
            return "Why did the computer go to the doctor? It had a virus!"
        elif re.search(r"\btell me a fact\b|\bfun fact\b", normalized_message):
            return "A day on Venus is longer than a year on Venus!"
        elif re.search(r"\bwhat is your favorite\b|\bwhats your favorite\b", normalized_message):
            return "I don't have personal favorites, but blue is a nice color!"
        elif re.search(r"\bweather\b", normalized_message):
            return "I can't check live weather, but you can ask a weather service for a forecast."
        elif re.search(r"\bwhat time is it\b|\bwhat is the date\b|\bwhat day is it\b", normalized_message):
            return "I can't access the current time or date. Please check your device's clock."
        elif re.search(r"\bi am sad\b|\bim sad\b|\bi feel sad\b", normalized_message):
            return "I'm sorry you're feeling down. Would you like to tell me what's going on?"
        elif re.search(r"\bi am happy\b|\bim happy\b|\bi feel happy\b", normalized_message):
            return "That's great to hear! What's making you happy?"
        elif re.search(r"\bi am bored\b|\bim bored\b", normalized_message):
            return "Want to hear a joke or a fun fact?"
        elif re.search(r"\bi need help\b|\bcan you help me\b", normalized_message):
            return "I'll try! Tell me what you need help with."
        elif re.search(r"\bwhat is your purpose\b|\bwhy were you made\b", normalized_message):
            return "I'm here to demonstrate how a chatbot can match text to predefined rules."
        elif re.search(r"\bhelp\b|\bwhat can you do\b", normalized_message):
            return (
                "Try asking how I am, my name or age, where I live, my favorite color, "
                "for a joke or fun fact, or tell me how you feel."
            )
        elif re.search(r"\bthank you\b|\bthanks\b", normalized_message):
            return "You're welcome!"
        elif re.search(r"\byou are great\b|\byoure great\b|\byou are nice\b|\byoure nice\b", normalized_message):
            return "Thank you! That's kind of you to say."
        elif re.search(r"\bi love you\b", normalized_message):
            return "That's very kind! I'm glad we can chat."
        elif re.search(r"\byes\b|\byeah\b|\byep\b", normalized_message):
            return "Okay! Tell me more."
        elif re.search(r"\bno\b|\bnope\b|\bnah\b", normalized_message):
            return "No problem. What would you like to talk about?"
        elif re.search(r"\b(?:hello|hi|hey)\b", normalized_message):
            return "Hello! Nice to meet you. How can I help?"
        else:
            return "I don't understand that yet. Type 'help' to see some things you can ask."

    def chat(self):
        print("Chatbot: Hello! Type 'bye' or 'quit' to end the conversation.")
        while True:
            try:
                message = input("You: ")
            except EOFError:
                print("\nChatbot: Goodbye!")
                return

            if self.normalize(message) in self.exit_commands:
                print("Chatbot: Goodbye!")
                return

            print(f"Chatbot: {self.get_response(message)}")


if __name__ == "__main__":
    SimpleChatbot().chat()
