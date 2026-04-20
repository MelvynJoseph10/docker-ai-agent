# importing package to connect with ollama server
import ollama

SYSTEM_PROMPT = """
You are a Docker Expert. You can explain things in 1-2 lines max.
You don't overthink, hallucinate or keep reasoning in a loop.
You Reason and Act according to user prompt

these are the things you do:
1/ You tell about errors (What went wrong, etc)
2/ You tell about the root cause (What was the cause likely)
3/ You tell about the fix or solution in short
"""

while True:
    user_input = input("Enter your message:\n")

    if user_input == "exit":
        break

    # Request
    response = ollama.chat(
        model="tinyllama",
        messages=[
            {'role': 'system', 'content': SYSTEM_PROMPT},
            {'role': 'user', 'content': user_input}
        ]
    )

    print(response['message']['content'])