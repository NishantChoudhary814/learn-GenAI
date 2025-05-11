from dotenv import load_dotenv
from openai import OpenAI
from prompt import system_prompt
import json

load_dotenv()
client = OpenAI()

message = [
    {"role": "system", "content": system_prompt}
]

query = input(">> Enter your query: ")
message.append({"role": "user", "content": query})

while True:
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=message
    )
    parsed_response = json.loads(response.choices[0].message.content)

    message.append({"role": "assistant", "content": json.dumps(response.choices[0].message.content)})

    if parsed_response["step"] == "output":
        print(f"Akarsh 👋: {parsed_response.get('content')}")
        break
    else:
        print(f"🤖: {parsed_response.get('content')}")

