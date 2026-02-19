import argparse
import sys
from openai import OpenAI

def main():
    parser = argparse.ArgumentParser(description="Simple OpenAI-compatible client for local models.")
    parser.add_argument("prompt", help="The prompt to send to the model.")
    parser.add_argument("--base_url", default="http://localhost:8000/v1", help="The base URL of the local server.")
    parser.add_argument("--model", default="user.Holo2-30B-A3B-GGUF", help="The model identifier to use.")
    parser.add_argument("--stream", action="store_true", help="Whether to stream the response.")

    args = parser.parse_args()

    client = OpenAI(
        base_url=args.base_url,
        api_key="lemonade", # Required but usually ignored by local servers
    )

    try:
        response = client.chat.completions.create(
            model=args.model,
            messages=[
                {"role": "user", "content": args.prompt}
            ],
            stream=args.stream
        )

        if args.stream:
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    print(chunk.choices[0].delta.content, end="", flush=True)
            print()
        else:
            print(response.choices[0].message.content)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
