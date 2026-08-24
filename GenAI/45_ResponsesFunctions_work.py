import json
from openai import OpenAI

client = OpenAI()

# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)

tools = [{
    "type": "function",
    "name": "get_current_weather",
    "description": "Get the current weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA"
            },
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
        },
        "required": [
            "location"
        ],
        "additionalProperties": False
    }
}]

input_messages=[{"role": "user", "content": "What is the weather like in Orlando, Florida today?"}]

response = client.responses.create(
    model="gpt-4o",
    input=input_messages,
    tools=tools
)

# Print the initial response, asking us to use a tool. 
print("Step 1: Initial result for weather in Orlando:")
print(response.output)


#OUTPUT:
# (OpenAI is asking us to make a call to the function and return it)
#[ResponseFunctionToolCall
#(arguments='{"location":"Orlando, FL","unit":"fahrenheit"}', 
#call_id='call_ets39HtY5x2rgeDc7HpBpVZV', 
#name='get_current_weather', 
#type='function_call', 
#id='fc_0069050be5346e60006a8c46ea98f487d2b4bd485b0b4561bc', 
#caller=None, namespace=None, status='completed')
]
# Attempt to get the tool it wants
print("\nStep 2: Call the tool it wants")
tool_call = response.output[0]
args = json.loads(tool_call.arguments)

# Attempt to call the tool it wants us to call
result = get_current_weather(args["location"], args["unit"])
print(result)

# Call openAI again. 
print("\nStep 3: Incorporate results into prompt")
input_messages.append(tool_call)  # append model's function call message
input_messages.append({           # append result message
    "type": "function_call_output",
    "call_id": tool_call.call_id,
    "output": str(result)
})

response_2 = client.responses.create(
    model="gpt-4o",
    input=input_messages,
    tools=tools,
)
print(response_2.output_text)
## OUTPUT ##
# The weather in Orlando, Florida today is 72°F, 
# with a sunny and windy forecast.