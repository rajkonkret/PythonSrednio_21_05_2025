import openai

class ChatBot():
    def __init__(self, model='gpt-3.5-turbo'):
        self.client = openai.OpenAI(api_key='')
        self.messages = []
        self.model = model

    def add_message(self, role, content):

        if role in ['user', 'assistant']:
            self.messages.append(
                {'role': role, 'content': content}
            )
        else:
            raise ValueError("Role must be 'user' or 'assistant")

    def get_response(self, user_messaage):
        self.add_message('user', user_messaage)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        print(response)
        model_messages = response.choices[0].message.content
        self.add_message('assistant', model_messages)
        return model_messages

bot =ChatBot()
if __name__ == '__main__':
    print("Starting")
    print(bot.get_response("Jak w python użyć lambda"))