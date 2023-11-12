from openai import OpenAI
import os

my_key = "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"
client = OpenAI(api_key=my_key)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)