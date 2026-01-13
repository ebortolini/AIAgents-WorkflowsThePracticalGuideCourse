import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def generate_x_post(usr_input: str) -> str:
    with open("post-examples.json", "r") as f:
        examples = json.load(f)

    examples_str = ""
    for i, example in enumerate(examples, 1):
        examples_str += f"""
        <example-{i}>
            <topic>
            {example['topic']}
            </topic>

            <generated-post>
            {example['post']}
            </generated-post>
        </example-{i}>
        """

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

       Here are some examples of topics and generated posts:
        <examples>
            {examples_str}
        </examples>

        Please use the tone, language, structure , and style of the examples provided above to generate a post that is engaging and relevant to the topic provided by the user.
        Don't use the content from the examples!
    """
    response = client.responses.create(model="gpt-4o", input=prompt)

    return response.output_text

def main():
    # user input => AI (LLM) to generate X post => output post

    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X post")
    print(x_post)

if __name__ == "__main__":
    main()