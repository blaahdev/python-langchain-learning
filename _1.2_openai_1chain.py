from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import argparse
from  dotenv import load_dotenv

load_dotenv()

# ------- OPTIONAL IF U WANNA GET INPUT FROM CLI------
parser = argparse.ArgumentParser()
parser.add_argument("--task", default="Return a list of numbers") # default optional if user doesnt provide value
parser.add_argument("--language", default="python")
args = parser.parse_args()
# ----------------------------------------------------


# llm = OpenAI(openai_api_key = API_KEY)
llm = OpenAI()

# 1. prompt template
prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables=["language", "task"]
)

# 2. chain
chain = LLMChain(
    llm=llm,
    prompt=prompt
)

# INPUT: dictionary setting the input value of the chain
# result = chain({
#     "language": "python",
#     "task": "return a list of numbers"
# })
result = chain({
    "language": args.language,
    "task": args.task
})
# OUTPUT: dictionary result will be a dictionary of all the input and the output
# by defaul the default output keyname is "text"
print(result)
print(result["text"])
"""
result::
{
'language': 'python', 
'task': 'return a list of numbers', 
'text': '\n\ndef get_numbers():\n    return [1, 2, 3, 4, 5]'}
"""