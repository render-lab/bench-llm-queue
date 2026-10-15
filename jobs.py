from openai import OpenAI


def summarize(text: str) -> str:
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Summarize the user's text in two sentences."},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content
