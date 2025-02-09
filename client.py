from openai import OpenAI
client = OpenAI()
api_key="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"

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
     ]
)

print(completion.choices[0].message)