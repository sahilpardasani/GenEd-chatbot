import os
import urllib.parse
import openai

openai.api_key = "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"  # Replace with your actual API key

# Define conversation history as an empty list
conversation_history = []

while True:
  user_text = input("Enter your message (or type 'exit' to end): ")

  if user_text.lower() == 'exit':
    break  # Exit the loop if the user types 'exit'

  # Append user message to the conversation history
  conversation_history.append({"role": "user", "content": user_text})

  try:
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-16k-0613",
      messages=conversation_history
    )

    if response is not None and response['choices'] and response['choices'][0]['message']:
      decoded_response = urllib.parse.unquote(response['choices'][0]['message']['content'])
      print(decoded_response)
      # Append AI message to the conversation history
      conversation_history.append({"role": "assistant", "content": decoded_response})
    else:
      print("Error: Empty response from OpenAI.")
  except Exception as e:
    print(f"Error: {str(e)}")

