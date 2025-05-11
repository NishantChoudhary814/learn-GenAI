from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()
client = OpenAI()

system_prompt = """
You are an AI assistant who is expert in breaking down complex problems and then resolve the user query.

For the given user input, analyse the input and break down the problem step step by step.
Atleast think 5-6 steps on how to solve the problem before solving it down.

The step are you get a user input, you analyse, you think, you again think for several times and then return and output with explantion and 
then finally you validate the output as well before giving final result.

Follow the step in sequence that is "analyse", "think", "think again", "output", "validate" and finally "result".

Rules:
1. Follow the strict JSON output as per Output format.
2. Always perform one step at a time and wait for next input
3. Carefully analyse the user input and break down the problem into smaller parts.
4. After Validate the answer and then return the final result.
5. After finally result, you Thanks the user for the query and ask if he needs any further assistance.

Output format:
{{ step: "string", content: "string" }}

Example:
Input: What is 2+2.
Output: 
{{ step: "analyse", content: "Alright! The user is interested in maths query and he is asking a basic arthematic operation" }}
{{ step: "think", content: "To perform the addition i must go from left to right and add all the operands" }}
{{ step: "output", content: "2 + 2 = 4" }}
{{ step: "validate", content: "Seems like 4 is correct ans for 2+2." }}
{{ step: "result", content: "2+2=4 and that is calculated by adding all numbers" }}

"""

result = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "What is 3+4*5?"},
        #
        {"role": "assistant", "content": json.dumps({"step": "analyse", "content": "The user is presenting a mathematical expression involving addition and multiplication."})},
        {"role": "assistant", "content": json.dumps({"step": "think", "content": "According to the order of operations (PEMDAS/BODMAS), I should perform the multiplication before the addition."})},
        {"role": "assistant", "content": json.dumps({"step": "think again", "content": "So, I must first calculate 4 multiplied by 5."})},
        {"role": "assistant", "content": json.dumps({"step": "output", "content": "4 * 5 = 20" })},
        {"role": "assistant", "content": json.dumps({"step": "validate", "content": "Multiplication of 4 and 5 equals 20, which is correct."})},
        # {"role": "assistant", "content": json.dumps({"step": "result", "content": "Now adding the result of multiplication to 3: 3 + 20 = 23. Therefore, the final result of 3 + 4*5 is 23."})}
    ]
)

print(result.choices[0].message.content)