import os
import openai

from dotenv import load_dotenv

load_dotenv()


def translate(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You will be provided with a sentence in Polish, and your task is to translate it into English."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['message']["content"]


if __name__ == '__main__':
    print(translate("Nazywam się Paweł i jestem programistą."))
