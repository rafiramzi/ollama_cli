import ollama
import time

# ANSI color codes
BLUE = "\033[94m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
RESET = "\033[0m"

client = ollama.Client()
model = "llama3.1:8b"

print(f"{BLUE}Ollama AI Chat CLI{RESET}")
print("Loading ...")

begin_prompt = "Hello"
start_time = time.time()
response = client.generate(model=model, prompt=begin_prompt)
end_time = time.time()

print(f"{BLUE}Ollama:{RESET} {WHITE}{response.response}{RESET}")
print(f"[Thinking time: {end_time - start_time:.2f} seconds]")

def chat(chat_input):
    start_time = time.time()
    response = client.generate(model=model, prompt=chat_input)
    end_time = time.time()
    thinking_time = end_time - start_time
    return response.response, thinking_time

def main():
    while True:
        chatbox = input(f"{YELLOW}You:{RESET} ")
        if chatbox.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        print("Thinking ...")
        chat_response, thinking_time = chat(chatbox)
        print(f"{BLUE}Ollama:{RESET} {WHITE}{chat_response}{RESET}")
        print(f"[Thinking time: {thinking_time:.2f} seconds]\n")

main()
