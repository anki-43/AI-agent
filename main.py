import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function
import json

def main() -> None:
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    if api_key == None:
        raise RuntimeError('emprt api key')

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    args = parser.parse_args()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    generate_content(client, messages, args.verbose)


def generate_content(client: OpenAI, messages: list, verbose: bool) -> None:
    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages= messages,
            tools=available_functions,
        )

        if verbose:
            # print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")

        print(f"Response: {response.choices[0].message.content}")

        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            print("Response:")
            print(message.content)
            return
        
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            result_message = call_function(tool_call, verbose)
            messages.append(result_message)
            if not result_message.get("content"):
                raise ValueError("Tool returned an empty content")

            if verbose:
                print(f"-> {result_message['content']}")

if __name__ == "__main__":
    main()