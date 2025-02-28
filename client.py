import argparse
import requests
from datetime import datetime

# Update this URL to your server's URL if hosted remotely
API_URL = "http://127.0.0.1:8000/predict"

def send_request(prompt):

    response = requests.post(API_URL, json={"prompt": prompt})
    if response.status_code == 200:
        filename = f"output-{datetime.now()}.png"
        
        with open(filename, "wb") as image_file:
            image_file.write(response.content)
        
        print(f"Image saved to {filename}")
    else:
        print(f"Error: Response with status code {response.status_code} - {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sends a prompt to the Flux server and receives the generated image")
    parser.add_argument("--prompt", required=True, help="Prompt to feed to the model")
    args = parser.parse_args()
    
    send_request(args.prompt)