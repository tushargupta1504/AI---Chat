Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def chatbot_response(user_input):
...     if "hello" in user_input:
...         return "Hi there! How can I assist you?"
...     elif "how are you" in user_input:
...         return "fine n you and ??"
...     elif "bye" in user_input:
...         return "Goodbye! Have a great day!"
...     elif "thanks" in user_input:
...         return "You're welcome!"
...     else:
...         return "I'm not sure how to respond to that."
... 
... def main():
...     print("Chatbot: Hi, I'm your simple chatbot. Ask me anything or say 'bye' to exit.")
... 
...     while True:
...         user_input = input("You: ").lower()
... 
...         if user_input == "bye":
...             print("Chatbot: Goodbye! Take care.")
...             break
... 
...         response = chatbot_response(user_input)
...         print("Chatbot:", response)
... 
... if __name__ == "__main__":
...     main()
