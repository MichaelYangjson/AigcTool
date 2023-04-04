import openai
import toml
from loguru import logger


# api_key = toml.load("../config.toml")["chatgbt"]["api_key"]


class ChatApi:
    models = {"gpt_3.5": "gpt-3.5-turbo", "gbt_4": "gpt-4"}
    __api_key = ""

    def __init__(self):
        self.__api_key = self.__api_key
        self.conversation_list = []
        # self.__api_key = __api_key
        # self.__api_model = model

    def get_api_key(self):
        return self.__api_key

    def get_api_model(self, key):
        return self.models[key]

    # 文字生成model
    def text_generation(self, content_dic, key):
        self.conversation_list.append(content_dic)
        openai.api_key = key
        model = self.get_api_model("gpt_3.5")
        completion = openai.ChatCompletion.create(
            model=model,
            messages=self.conversation_list
        )
        answer = completion["choices"][0]["message"]["content"]
        logger.info("class ChatApi text_generation success answer:{answer}", answer=answer)
        self.conversation_list.append({"role": "assistant", "content": answer})
        return completion, self.conversation_list


# 文字生成model
# def text_generation(content):
#     chat_obj = ChatApi()
#     openai.api_key = chat_obj.get_api_key()
#     model = chat_obj.get_api_model("gpt_3.5")
#     completion = openai.ChatCompletion.create(
#         model=model,
#         messages=[{"role": "user", "content": content}]
#     )
#     return completion


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


# chat_obj = ChatApi()
# while True:
#     input_user = input("请输入你要问的问题")
#     if input_user == "exit":
#         print(input_user)
#         break
#     else:
#
#         result,chat = chat_obj.text_generation(input_user, "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")
#         res = result["choices"][0]["message"]["content"]
#         print(res)

def text_call(content, key):
    chat_obj = ChatApi()
    result, conversation_list = chat_obj.text_generation(content, key)
    res = result["choices"][0]["message"]["content"]
    usage = result["usage"]
    logger.info("text_call usage: {usage}, res: {res}", usage=usage, res=res)
    return usage, conversation_list

# text_call("你是谁？", "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")
