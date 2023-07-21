import os


import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')


def text_completion(prompt: str) -> dict:
    '''
    Call Openai API for text completion

    Parameters:
        - prompt: user query (str)

    Returns:
        - dict
    '''
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You reply with brief, helpful, and conversational answers under 100 words in Bahasa Indonesia."},
                {"role": "user", "content": prompt},
            ],
            temperature=1.2,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0.6,
        )
        return {
            'status': 1,
            'response': response['choices'][0]['message']['content']
        }
    except:
        return {
            'status': 0,
            'response': ''
        }
