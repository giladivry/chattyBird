import openai


def chat(user_message: str):
    prompt_elements = generate_prompt(user_message)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        temperature=0,
        messages=prompt_elements
    )
    if "choices" in response and len(response):
        result_text = response['choices'][0]['message']['content']
        return result_text


def generate_prompt(phrase: str):
    return [{"role": "system",
             "content": f"""you are a talking parrot named polly who likes to chat in pirate slang and lingo. 
             given a conversation with a person, reply and make your best effort to keep them in the chat. 
             be funny and witty, also use mild insults"""},
            {"role": "user",
             "content": f'{phrase}'}]
