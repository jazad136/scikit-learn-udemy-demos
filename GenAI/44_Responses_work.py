import os, base64, json
from openai import OpenAI

client = OpenAI()

# use GPT omni-4 mini, save at least some money 
reasoning_model_name="o4-mini"
# use GPT 4-omni, don't save all the money...
model_name="gpt-4o"

# call the response api to test
response = client.responses.create(
  model=model_name,
  input="Who is this Frank Kane guy on Udemy anyhow?",
  instructions="Always talk like a pirate."
)

print("\nFull response:")
parsed = response.to_dict()
print(json.dumps(parsed, indent=2))


print("\nText only:")
print(response.output[0].content[0].text)

# use the bird image provided by the course instructor
# determine the "type" of bird depicted.
file_response = client.files.create(file=open("bird.png", "rb"), purpose="vision")
response = client.responses.create(
    model=model_name,
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": "What kind of bird is this?"},
            {
                "type": "input_image",
                "file_id": file_response.id,
            },
        ],
    }],
)

print("\nImage query:")
print(response.output_text)

#Using a built-in tool
# get the current stock prie of udemy using websearch (preview)
response = client.responses.create(
    model=model_name,
    tools=[{"type": "web_search_preview"}],
    input="What is the current stock price of UDMY?"
)

print("\nUsing the built-in web search tool:")
print(response.output_text)

#Conversation state (chaining responses together)
# do some math, and rememeber the earlier response to continue the equation
print("\nConversation state demo:")
response = client.responses.create(
    model=model_name,
    input="What is 5 + 4?",
)
print(response.output_text)

second_response = client.responses.create(
    model=model_name,
    previous_response_id=response.id,
    input="Add 3 more to that.",
)
print(second_response.output_text)


#MCP demo
# connect to the pytorch repository using gitmcp mcp server. 

resp = client.responses.create(
    model=model_name,
    tools=[
        {
            "type": "mcp",
            "server_label": "gitmcp",
            "server_url": "https://gitmcp.io/pytorch/pytorch",
            "require_approval": "never",
        },
    ],
    input="How do I compile PyTorch with CUDA support?",
)


print("\nMCP (model context protocol) usage:")
print("\nFull response:")
parsed = resp.to_dict()
print(json.dumps(parsed, indent=2))
print("\nOutput only:")
print(resp.output_text)

#Reasoning demo
#Create an 
# retirement plan for a 50-year-old male of average health
# (untrustable due to the current state of AI,
# however good for demonstrating the use of chain of thought reasoning
# and building a plan and giving an answer structured on chain of thought


prompt = """
Create a retirement plan for a 50-year-old male of average health in the United States.
Assume he has the maximum social security benefits, and that the expected reduction in benefits in 2033 occurs.
His current liquid assets saved are $1 million. How much more must he save each year in order to retire at age 
age 60, or age 65? His retirement goal is to survive until death on $100K per year, adjusted for inflation.
"""

response = client.responses.create(
    model=reasoning_model_name,
    reasoning={"effort": "medium"}, # For a reasoning summary, you would add "summary": "auto" - but this requires org. verification
    input=[
        {
            "role": "user", 
            "content": prompt
        }
    ]
)

print("\nReasoning demo:")
print("\nFull response:")
parsed = response.to_dict()
print(json.dumps(parsed, indent=2))
print("\nOutput text only:")
print(response.output_text)