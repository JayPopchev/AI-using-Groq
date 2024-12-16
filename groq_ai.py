import traceback
from groq import Groq

# Initialize Groq API client
client = Groq(
    api_key='your_api_key_here',  # Replace with your actual API key
)


# Function to get chat completion from Groq API
def get_ai_response(user_input):
    try:
        # Try to send the request to the API
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": user_input}],
            model="llama3-8b-8192",  # Ensure this model is available and valid
        )
        # Return the chat response
        return chat_completion.choices[0].message.content

    except Exception as e:
        # Log the error message and include traceback for debugging
        error_message = f"Error: {str(e)}\n"
        error_message += f"Traceback: {traceback.format_exc()}"
        return error_message


# Main loop for user input
while True:
    user_input = input("You: ")

    # Exit condition for the loop
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! 👋")
        break

    # Get AI response and handle errors if any
    response = get_ai_response(user_input)
    print("AI: " + response)