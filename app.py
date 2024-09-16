import openai
import os
import chainlit as cl
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT, CONTEXT
from langsmith import traceable
from langsmith.wrappers import wrap_openai

# Load environment variables
load_dotenv()
ENABLE_SYSTEM_PROMPT = True

configurations = {
    "mistral_7B_instruct": {
        "endpoint_url": os.getenv("MISTRAL_7B_INSTRUCT_ENDPOINT"),
        "api_key": os.getenv("RUNPOD_API_KEY"),
        "model": "mistralai/Mistral-7B-Instruct-v0.2"
    },
    "mistral_7B": {
        "endpoint_url": os.getenv("MISTRAL_7B_ENDPOINT"),
        "api_key": os.getenv("RUNPOD_API_KEY"),
        "model": "mistralai/Mistral-7B-v0.1"
    },
    "openai_gpt-4": {
        "endpoint_url": os.getenv("OPENAI_ENDPOINT"),
        "api_key": os.getenv("OPENAI_API_KEY"),
        "model": "gpt-4"
    }
}

# Choose configuration
# config_key = "openai_gpt-4"
config_key = "mistral_7B_instruct"
# config_key = "mistral_7B"

# Get selected configuration
config = configurations[config_key]

# Initialize the OpenAI async client
client = wrap_openai(openai.AsyncClient(api_key=config["api_key"], base_url=config["endpoint_url"]))

gen_kwargs = {
    "model": config["model"],
    "temperature": 0.3,
    "max_tokens": 500
}

@cl.on_message
@traceable
async def on_message(message: cl.Message):
    #Maintain an array of messages in the user session
    message_history = cl.user_session.get("message_history", [])

    if ENABLE_SYSTEM_PROMPT and (not message_history or message_history[0].get("role") != "system"):
        filled_prompt = SYSTEM_PROMPT
        filled_prompt += "\n" + CONTEXT
        message_history.insert(0, {"role": "system", "content": filled_prompt})


    message_history.append({'role': 'user', 'content': message.content})

    response_msg = cl.Message(content="")
    await response_msg.send()

    # Pass in the full message history for each request
    stream = await client.chat.completions.create(
        messages=message_history, stream=True, **gen_kwargs
    )

    async for part in stream:
        if token := part.choices[0].delta.content or "":
            await response_msg.stream_token(token)
    await response_msg.update()

    # Record the AI's response in the history
    message_history.append(
        {'role':'assistant','content':response_msg.content}
    )
    cl.user_session.set("message_history",message_history)




