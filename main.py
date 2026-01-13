import requests
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_x_post(usr_input: str) -> str:
    prompt = f"""
        You are an expert social media manager, and you excel at crafting viral and highly engaging
        post for X (formerly Twitter).

        Your task is to generate a post that is concise, pactful, and tailored to the topic provided by the user.
        Avoid using hashtags and lots of emojis.

        Keep the post short and focused, structured it in a clean, readable way.

        Hers is the topic for which you need to generate a post: 
        <topic>
        {usr_input}
        </topic>
    """
    payload = {
        "model": "gpt-4o",
        "input": prompt
    }
    
    response = requests.post(
        "https://api.openai.com/v1/responses",
        json=payload,
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
    )

    response_json = response.json().get("output", [{}])[0].get("content", "")[0].get("text", "")
    return response_json

            

def main():
    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X post:")
    print(x_post)



if __name__ == "__main__":
    main()
