import requests
from config import  HF_API_KEY
from colorama import Fore, Style, init

init(autoreset=True)

DEFAULT_MODEL = "google/pegasus-xsum"
def build_api_url(model_name):
    return f"https://api-inference.huggingface.co/models/{model_name}"
def query(payload, model_name=DEFAULT_MODEL)
    """

    Sends a POST request to the Hugging Face API using the specified model

    """

    api_url = build_api_url(model_name)
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    reponse = requests.post(api_url, headers=headers, json=payload)
    return response.json()

def summarize_text(text, min_length, max_length, model_name=DEFAULT_MODEL):
    payload = {
        "inputs": text, 
        "parameters": {"min_length": min_length, "max_length": max_length}
    }

    print(Fore.BLUE + Style.BRIGHT + f"\n???? Performing AI summarization using model: {model_name}")

    result = query(payload, model_name=model_name)

    if isinstance(result, list) and result and "summary_text" in result[0]:
        return result[0]["summaary_text"]
    else:
        print(Fore.RED + "Error in summarization response:", result)
        return None

if __name__ == "__main__":
    print(Fore.YELLOW + Style.BRIGHT + "???? Hi there! What's your name?")

    user_name - input("Your name: ").strip()
    if not user_name:
        user_name = "User"
    print(Fore.GREEN + f"Welcome, {user_name}! Let's give your text some AI magic.")
    