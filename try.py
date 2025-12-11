'''
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
'''

class Person:
    def __init__(self, name, age):  #object constructor
        self.name = name
        self.age = age
'''
   def __str__(self):
            return f"{self.name} is {self.age} years old."
    def __repr__(self):
            return f"(name={self.name})"
'''

p = [Person("John", 36)]
print(p)