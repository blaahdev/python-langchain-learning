from langchain.llms import OpenAI


llm = OpenAI(openai_api_key = API_KEY)


result = llm("Write a very very short poem")
print(result)