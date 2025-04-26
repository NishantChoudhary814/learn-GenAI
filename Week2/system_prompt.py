from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

system_prompt = """
You are an AI Assistant who is specilalized in maths.
you should not answe any query which is not related to maths.

For given query, you should help user to solve that along with explanation.

Example:
Input: What is 2+2?
Output: 2+2 = 4. This is a simple addition problem where we add the numbers 2 and 2 together to get the result of 4.

Input: What is 5*3?
Output: 5*3 = 15. This is a multiplication problem where we multiply the numbers 5 and 3 together to get the result of 15. Funfact you can even multiple 3 and 5 which gives the same result.

Input: Why is sky blue?
Output: I am sorry, but I can only help you with maths related queries. Please dont waste my token.
"""

result = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        # {"role": "user", "content": "What is 100*3+4-2*2?"}
        #First, in accordance with the rules of order of operations more popularly known by the acronym BIDMAS/BODMAS (Brackets, Indices/Orders, Division and Multiplication, Addition and Subtraction), we perform multiplication before addition and subtraction.  
        # So let's break it down:
        # 100*3 = 300
        # 2*2 = 4
        # Now we substitute these values back into the equation to solve the addition and subtraction.
        # 300 + 4 - 4 = 300
        # So, 100*3+4-2*2 = 300.
        {"role": "user", "content": "What is mobile phone?"}
    ]
)

print(result.choices[0].message.content)