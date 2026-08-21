import os
from openai import OpenAI

client = OpenAI()

prompt = input("Enter your prompt: ")
# My prompt: What is the meaning of life? 

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ]
)

print("\n" + completion.choices[0].message.content)
# Output from the model: 
    
# The meaning of life is a philosophical question that has been debated 
# for centuries. It ultimately depends on one's personal beliefs and 
# values. Some people find meaning in relationships, experiences, personal 
# growth, helping others, or spiritual beliefs. Others may think that life
#  has no inherent meaning and that it is up to each individual to create 
#  their own purpose.

print("\nComplete response message:\n")

# print the complete call
print(completion)

## OUTPUT FROM THE COMPLETION OBJECT
# ChatCompletion(id='chatcmpl-EEyoaN3nsGUeNZtE2mHMQqf6Ka4Ew', 
# choices=[Choice(finish_reason='stop', index=0, logprobs=None, 
# message=ChatCompletionMessage(content="The meaning of life 
# is a philosophical question that has been debated for centuries. 
# It ultimately depends on one's personal beliefs and values. Some 
# people find meaning in relationships, experiences, personal growth, 
# helping others, or spiritual beliefs. Others may think that life has 
# no inherent meaning and that it is up to each individual to create 
# their own purpose.", refusal=None, role='assistant', annotations=[], 
# audio=None, function_call=None, tool_calls=None))], created=1787239072, 
# model='gpt-3.5-turbo-0125', object='chat.completion',
# metadata=None, moderation=None, service_tier='default', 
# system_fingerprint=None, 
# usage=CompletionUsage(completion_tokens=68, prompt_tokens=24, 
# total_tokens=92, 
# completion_tokens_details=CompletionTokensDetails(
# accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, 
# rejected_prediction_tokens=0, text_tokens=None), 
# prompt_tokens_details=PromptTokensDetails(audio_tokens=0, 
# cache_write_tokens=None, cached_tokens=0, image_tokens=None, 
# text_tokens=None)))

# second prompt
# same syntax
# ... 
# change the system prompt giving it more explicit directions for 
# what to do 

prompt = input("\nEnter a string for sentiment analysis: ")


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
# OUTPUT
# Positive sentiment

# print out the complete message so we can tell what we're looking at
print("\nComplete response message:\n")
print(completion)
## OUTPUT FROM THE COMPLETION OBJECT (STILL LONG)
# ChatCompletion(id='chatcmpl-EEyrjfSpm9Vb0Wd2aPEHqp0eLV0nz', 
# choices=[Choice(finish_reason='stop', index=0, logprobs=None, 
# message=ChatCompletionMessage(content='Positive sentiment', 
# refusal=None, role='assistant', annotations=[], audio=None,
# function_call=None, tool_calls=None))], created=1787239267, 
# model='gpt-3.5-turbo-0125', object='chat.completion', metadata=None, 
# moderation=None, service_tier='default', system_fingerprint=None, 
# usage=CompletionUsage(completion_tokens=2, prompt_tokens=26, 
# total_tokens=28, completion_tokens_details=CompletionTokensDetails
# (accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, 
# rejected_prediction_tokens=0, text_tokens=None), 
# prompt_tokens_details=PromptTokensDetails(
# audio_tokens=0, cache_write_tokens=None, cached_tokens=0, 
# image_tokens=None, text_tokens=None)))

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
# OUTPUT
# Why did the scarecrow win an award?
# 
# Because he was outstanding in his field!

