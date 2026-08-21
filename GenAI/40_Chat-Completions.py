import os
from openai import OpenAI

client = OpenAI()

prompt = input("Enter your prompt: ")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ]
)

print("\n" + completion.choices[0].message.content)

print("\nComplete response message:\n")
# print the complete call
print(completion)

# second prompt
prompt = input("\nEnter a string for sentiment analysis: ")
# same syntax
# ... 
# change the system prompt giving it more explicit directions for 
# what to do 


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
      # Whatever I say as a user
      # classify it as positive or negative sentiment
    {"role": "system", "content": "Classify user messages as positive or negative sentiment."},
    {"role": "user", "content": prompt}
  ]
)

# print out the message
print("\n" + completion.choices[0].message.content)

# print out the complete message so we can tell what we're looking at
print("\nComplete response message:\n")
print(completion)

# this time specify a temperature, 
# so we can be pretty sure to get the same joke every time. 
print("\nTell me a joke (with low temperature)")
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  temperature = 0.2,
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a joke."}
  ]
)

print("\n" + completion.choices[0].message.content)

