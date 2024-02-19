import os
import openai
import requests

api_key = "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"
openai.api_key = api_key

# address on which fastAPI going to run 
url = "http://127.0.0.1:8000/chat"

# Method to interact with bot
def chat_with_bot():
    print("Enter end to exit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "end":
            print("chat Ended...")
            break

        payload = {"user_input": user_input}

        # Sending a POST request to the chatGPT
        response = requests.post(url, json=payload)

        # Getting reply from GPT
        if response.status_code == 200:
            bot_reply = response.json()["bot_reply"]
            print("Bot:", bot_reply)
        else:
            print("Error:", response.text)

# Start chatting
if __name__ == "__main__":
    chat_with_bot()
