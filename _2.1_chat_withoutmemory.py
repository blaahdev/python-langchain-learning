from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chat_models import ChatOpenAI # observe, you are NOT importing OpenAI from langchain.llms 
from langchain.chains import LLMChain
from dotenv import load_dotenv

# ------- LOADING ENV
load_dotenv()

# ----------- INITIATING (0)
llm = ChatOpenAI()

# ----------- CHAIN (1)
# 1. Creating the prompt template
# observe: regular PromptTemplate(template="" , input_variables=[])
# observe: ChatPromptTemplate(messages=[], input_variables=[])
prompt = ChatPromptTemplate(
      messages=[
        HumanMessagePromptTemplate.from_template("{content}")
    ],
    input_variables=["content"]
)

# 2. Creating the chain
chain = LLMChain(llm=llm, prompt=prompt)

# -----------GETTING CHAT MESSAGES FROM USER

while True:
    content = input(">>")
    result = chain({"content": content})
    print(result["text"])