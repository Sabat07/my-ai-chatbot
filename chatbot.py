
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: Gemini API key not found.")
    raise SystemExit(1)

client = genai.Client(api_key=api_key)

print("=" * 40)
print("          MY AI CHATBOT")
print("=" * 40)
print("Powered by Google Gemini")
print("Type 'exit' to close the chatbot.")

previous_id = None

while True:
    user_message = input("\nYou: ").strip()

    if user_message.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    if not user_message:
        continue

    try:
        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            input=user_message,
            previous_interaction_id=previous_id,
        )

        print("\nAI:", interaction.output_text)
        previous_id = interaction.id

    except Exception as error:
        print("\nSomething went wrong:", error)
