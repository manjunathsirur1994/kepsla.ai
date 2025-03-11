import os
import json
import configuration
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("OPENAI_API_KEY")

from tools import tool
client = OpenAI(api_key=key)

from tool_functions import get_ticket

config = configuration.load_config()
entered_text = config["Prompt"]


def call_function(name, args):
    if name == "ticket_generator":
        return get_ticket(**args)


messages=[{"role": "system", "content": entered_text}]
messages.append({"role": "user", "content": 'tv is not working in room 223'})

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tool
)

if completion.choices[0].message.tool_calls:
    for tool_call in completion.choices[0].message.tool_calls:
        name = tool_call.function.name
        print(f"tool called: {name}")
        args = json.loads(tool_call.function.arguments)

        result = call_function(name, args)
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result
        })
else:
    print('no tool called')
    
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tool,
)

print(completion.choices[0].message)
print(messages)
