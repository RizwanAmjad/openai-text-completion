from dotenv import load_dotenv, dotenv_values
# from pychatgpt import Chat, OpenAI, Options
#
# load_dotenv()
#
# environment_variables = dotenv_values()
#
# EMAIL = environment_variables['EMAIL']
# PASSWORD = environment_variables['PASSWORD']
#
# # generate the auth token
# OpenAI.Auth(email_address=EMAIL, password=PASSWORD).save_access_token(access_token="")
# # create the chat gpt object
# chat = Chat(email=EMAIL, password=PASSWORD)

import openai
openai.api_key = "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"

completion = openai.Completion()


def generate_message_for_gpt(messages: list, suggestion_count: int):
    message = f"Please Suggest {suggestion_count} replies\n"
    for item in messages:
        message += f"{item[0]} says {item[1]}\n"
    return message


def get_reply_suggestions(messages: list, suggestion_count=3):
    message = generate_message_for_gpt(messages, suggestion_count)
    reply = completion.create(
        prompt=message, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    return reply.choices[0].text

