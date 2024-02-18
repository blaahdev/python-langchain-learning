from langchain.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chat_models import ChatOpenAI # observe, you are NOT importing OpenAI from langchain.llms 
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# ------- LOADING ENV
load_dotenv()

# ----------- INITIATING (0)
llm = ChatOpenAI()
# memory_key is name of messagesList variable
# return_messages=True means you are forcing chatgpt to return an OBJECT with HumanMessage("What is 1+1?") and AIMessage("2") instead of plain string
memory = ConversationBufferMemory(memory_key="messagesList", return_messages=True)

# ----------- CHAIN (1)
# 1. Creating the prompt template
# observe: regular PromptTemplate(template="" , input_variables=[])
# observe: ChatPromptTemplate(messages=[], input_variables=[])
prompt = ChatPromptTemplate(
      messages=[
        MessagesPlaceholder(variable_name="messagesList"),  # additional line needed to convert messagesList from memory and "spread" into the PromptTempalte
        HumanMessagePromptTemplate.from_template("{content}") #<-- to append new input from user
    ],
    input_variables=["content", "messagesList"]
)

# 2. Creating the chain
chain = LLMChain(
    llm=llm, 
    prompt=prompt,
    memory=memory # <-- observe
)

# -----------GETTING CHAT MESSAGES FROM USER

while True:
    content = input(">>")
    result = chain({"content": content})
    print(result["text"])