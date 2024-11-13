from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_type = "azure"
AZURE_ENDPOINT = "https://aoai-llmagent.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
API_KEY = ""

def get_completion_from_messages(system_message, user_message, model="gpt-4", temperature=0, max_tokens=500) -> str:

    messages = [
        {'role': 'system', 'content': "sqlite DB and schema follows :" + system_message},
        {'role': 'user', 'content': f"{user_message}"}
    ]
    
    
    client = openai.AzureOpenAI(
            azure_endpoint=AZURE_ENDPOINT,
            azure_deployment="gpt-4",
            api_key=API_KEY,
            api_version="2023-09-01-preview"
        )


    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    system_message = "You are a helpful assistant"
    user_message = "Hello, how are you?"
    print(get_completion_from_messages(system_message, user_message))
