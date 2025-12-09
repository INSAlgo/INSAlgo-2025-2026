import urllib.request
import urllib.parse
import json
import sys

def fetch_available_models():
    try:
        req = urllib.request.Request('http://localhost:11434/api/tags')
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                return [model['name'] for model in data['models']]
            else:
                raise ValueError(f"Failed to fetch models: HTTP {response.status}")
    except Exception as e:
        raise ValueError(f"Connection error: {str(e)}")

def select_model(available_models):
    print("Available models:")
    for i, model in enumerate(available_models, 1):
        print(f"{i}. {model}")
    print("\nSelect a model by number OR type a model name directly:")
    while True:
        choice = input("Enter number or model name: ").strip()
        if not choice:
            print("Please enter a model name or number.")
            continue
        
        # Try to parse as number first
        try:
            number_choice = int(choice)
            if 1 <= number_choice <= len(available_models):
                return available_models[number_choice - 1]
            else:
                print("Invalid choice. Please select a valid number.")
                continue
        except ValueError:
            # If not a number, treat as model name
            return choice

def send_message(model, message):
    try:
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": message}],
            "stream": True
        }
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request('http://localhost:11434/api/chat', data=data, headers={'Content-Type': 'application/json'})
        first_token = True
        with urllib.request.urlopen(req) as response:
            for line in response:
                line = line.decode('utf-8').strip()
                if line:
                    data = json.loads(line)
                    if 'message' in data and 'content' in data['message']:
                        if first_token:
                            first_token = False
                            print("AI: ", end='', flush=True)
                        print(data['message']['content'], end='', flush=True)
    except Exception as e:
        print(f"Error: {str(e)}")

def chat_loop(model):
    print("Chat client started. Type 'exit' to quit.")
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                print("Please enter a message.")
                continue
            if user_input.lower() == 'exit':
                print("Exiting chat.")
                break
            send_message(model, user_input)
            print()  # New line after streaming
        except KeyboardInterrupt:
            print("\nExiting chat.")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    try:
        available_models = fetch_available_models()
        if not available_models:
            raise ValueError("No models available.")
        selected_model = select_model(available_models)
        print(f"Using model: {selected_model}")
        chat_loop(selected_model)
    except ValueError as e:
        print(e)
        sys.exit(1)