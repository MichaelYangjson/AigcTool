from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import (
    initialize_agent,
    load_tools,
)
from langchain.chains import (
    LLMChain,
)
from langchain.prompts import PromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, \
    ChatPromptTemplate
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.schema import HumanMessage

# chat = ChatOpenAI(temperature=0, openai_api_key="",
#                   model_name="gpt-3.5-turbo")
# text = "What would be a good company name for a company that makes colorful socks?"
#
# template = "You are a helpful assistant that translates {input_language} to {output_language}."
# system_message_prompt = SystemMessagePromptTemplate.from_template(template)
# human_template = "{text}"
# human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
# chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
#
# chain = LLMChain(llm=chat, prompt=chat_prompt)
#
# print(chain.run(input_language="English", output_language="French", text="I love programming."))


chat = ChatOpenAI(streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), verbose=True,
                  temperature=0, openai_api_key="")
resp = chat([HumanMessage(content="Write me a song about dog.")])
print(resp)
