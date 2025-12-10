import openai

# Set your API key
openai.api_key = "YOUR_API_KEY_HERE"

# Call the GPT model
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain virtual environments in Python."}
    ]
)

# Print the AI's response
print(response.choices[0].message.content)
