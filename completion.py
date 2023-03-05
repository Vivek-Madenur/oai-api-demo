import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="what is your name?",
  temperature=0.7,
  max_tokens=1068,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)