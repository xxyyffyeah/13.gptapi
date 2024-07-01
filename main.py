from openai import OpenAI
import os
print(os.environ.get("BASE_URL"))



client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),base_url=os.environ.get("BASE_URL"))
def get_response(prompt):
  completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": prompt}
    ]
  )
  return completion.choices[0].message
question = input("Ask your question.\n")
print(get_response(question))


