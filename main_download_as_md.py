import sys
import os
import time
import requests

# Run "uv sync" to install the below packages
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

def download_as_md(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    response_html = requests.get(url)
    if response_html.status_code != 200:
        print(f"Failed to fetch URL: {url}")
        return
    html_content = response_html.text
    response = client.responses.create(
        # using gpt-4o-mini because it's great for summarization & extraction tasks (and cheap!)
        model="gpt-4o-mini",
        input=f"""
            You are a web post reader. Your function is to convert the provided HTML content of a post to markdown.

            The HTML content is:
            <html>
            {html_content}
            </html>
        """
    )

    text = response.output_text

    # save to a file:
    filename = str(int(time.time())) + ".md"
    filepath = os.path.join(dest_folder, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py url")
        sys.exit(1)
    download_as_md(sys.argv[1], "example_posts")

if __name__ == "__main__":
    main()