import sys
from openai import OpenAI
client = OpenAI()

class WordifyLLM():
    def __init__(self, user_input, model="gpt-3.5-turbo-0125", type="idiom"):
        self.user_input = user_input
        self.model = model 
        self.type = type
    
    def run_moderation(self):
        response_moderation = client.moderations.create(
            input=self.user_input
        )

        harmful_input_flag = response_moderation.results[0].flagged

        return harmful_input_flag

    def run_reverse_dictionary(self):
        response = client.chat.completions.create(
        model=self.model,
        messages=[
            {
            "role": "system",
            "content": [
                {
                "type": "text",
                "text": "Imagine yourself as the English Dictionary, suggest a list of 5 words that best describe the input sentence. Just output the words, nothing else."
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": self.user_input
                }
            ]
            }
        ],
        temperature=0.75,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        return response.choices[0].message.content
    
    def run_idiom_explanation(self):
        response = client.chat.completions.create(
        model=self.model,
        messages=[
            {
            "role": "system",
            "content": [
                {
                "type": "text",
                "text": "Explain the meaning of this idiom in one sentence and start your response with \"This idiom\""
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": self.user_input
                }
            ]
            }
        ],
        temperature=0.5,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        return response.choices[0].message.content
    
    def main(self):
        if self.run_moderation():
            return "Harmful/insensitive input. Please retry."
        
        if self.type=="idiom":
            return self.run_idiom_explanation()
        elif self.type=="reverse":
            return self.run_reverse_dictionary()
