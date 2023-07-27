import os
import openai

from dotenv import load_dotenv

load_dotenv()


def question_generator(q_number, question, level):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Create a list of {0} questions and answers for my technical interview with level {1} and position {2}"
        .format(q_number, level, question),
        temperature=0.5,
        max_tokens=1400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']


def technical_question(level, position):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are technical recruiter"
            },
            {
                "role": "user",
                "content": "Create for me code exercise in {0} for {1} on  my technical interview  and give solution:"
                           "\n\n###\nexercise:\nsolution:".format(
                    position, level)
            }
        ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['message']["content"]
