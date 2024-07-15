import openai
from rhombus_project.settings import OPENAI_APIKEY

class RegexService:
    def generate_regex(description):
        client = openai.OpenAI(api_key=OPENAI_APIKEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "Generate a JSON object that contains the specified column name, regex pattern, and replacement term for the user's request. The JSON object should clearly label each part: column name, regex pattern, and replacement term."},
                {"role": "user", "content": description}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
