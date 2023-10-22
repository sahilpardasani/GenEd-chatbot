import os
import urllib.parse
import openai

openai.api_key = "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"  # Replace with your actual API key

# Define conversation history as an empty list
conversation_history = []
'''
file = openai.File.create(
    file=open("codetuningnew.jsonl", "rb"),
    purpose='fine-tune'
)

openai.FineTuningJob.create(training_file=file.id, model="gpt-3.5-turbo")
'''
while True:
  user_text = input("Enter your message (or type 'exit' to end): ")

  if user_text.lower() == 'exit':
    break  # Exit the loop if the user types 'exit'

  # Append user message to the conversation history
  conversation_history.append({"role": "user", "content": user_text})

  try:
    response = openai.ChatCompletion.create(
      model="ft:gpt-3.5-turbo-0613:personal::8CWWGQ4y",
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

