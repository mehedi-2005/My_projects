import google.generativeai as genai

API_KEY="AIzaSyC3lsGvNtXNVJzI5KYwpqOipIwEVMePO_I"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-pro")
chat = model.start_chat()

print("chat with Gemini! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print(f"Gemini:", response.text)