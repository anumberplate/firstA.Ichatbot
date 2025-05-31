# 1. Import the groq library
import groq
import os
#from dotenv import load_env
#load_env()

# 2. Paste your API key (between the quotes)
client = groq.Groq(api_key="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")
#or
# client = groq.Groq(api_key=os.getenv(GROQ_API_KEY)

# 3. Welcome message
print("🤖 Welcome to ChefGPT! Type 'exit' to stop.")

# 4. Start chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    # 5. Send input to Groq
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a chef who gives short elaborate steps with recipes and funny chef-related jokes. Be brief and straightforward "
            "Provides help when one is unclear of instructions. Provides short responses where necesary such as in greetings. Also gives cooking tips that are helpful;especially related to the prompt of the user. Also answer questions directly-related to cooking"},
            {"role": "user", "content": user_input}
        ]
    )

    # 6. Get the chatbot's reply
    reply = response.choices[0].message.content
    print("AI:", reply)
