from apikeys import apikey
import os
from openai import OpenAI as oa

client = oa(api_key=apikey)


def chat(prompt):
    r = client.chat.completions.create(model="gpt-3.5-turbo",
                                       messages=[{"role": "user", "content": prompt}])

    return r.choices[0].message.content.strip()


if __name__ == '__main__':
    while True:
        user_input = input('you: ')
        response = chat(user_input)
        print(f'chatty: {response}')
