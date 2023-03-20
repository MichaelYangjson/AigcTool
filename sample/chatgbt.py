import openai
import os


class ChatApi:
    models = {"gpt_3.5": "gpt-3.5-turbo", "gbt_4": "gpt-4"}

    __api_key = "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"

    def __init__(self):
        self.__api_key = self.__api_key
        # self.__api_key = __api_key
        # self.__api_model = model

    def get_api_key(self):
        return self.__api_key

    def get_api_model(self, key):
        return self.models[key]


# 文字生成model
def text_generation(content):
    chat_obj = ChatApi()
    openai.api_key = chat_obj.get_api_key()
    model = chat_obj.get_api_model("gpt_3.5")
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": content}]
    )
    return completion


# for key in completion:
#     print(key)

# 图片生成model
def image_generation(prompt, size, number):
    chat_obj = ChatApi()
    openai.api_key = chat_obj.get_api_key()
    response = openai.Image.create(
        prompt=prompt,
        n=number,
        size=size
    )
    image_url = response['data'][0]['url']
    print(image_url)


# prompt = "a handsome boy who can dance"
# size = "1024x1024"
# image_generation(prompt, size, 1)


input = input("请输入你要问的问题")
result = text_generation(input)
res = result["choices"][0]["message"]["content"]
print(res)
