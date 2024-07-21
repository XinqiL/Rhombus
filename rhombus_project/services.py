import openai
from rhombus_project.settings import OPENAI_APIKEY

class RegexService:
    def generate_regex(description):
        client = openai.OpenAI(api_key=OPENAI_APIKEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "Create a JSON object that explicitly contains three key-value pairs: column_name, regex_pattern, and replacement_term, as specified by the user. Each key should be distinctly named and aligned with the user's request. The JSON object must be structured to clearly delineate these parts"},
                {"role": "user", "content": description}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
