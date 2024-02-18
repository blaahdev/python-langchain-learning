from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from dotenv import load_dotenv
import argparse

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--language", default="Python")
parser.add_argument("--task", default="function that print hello")
args = parser.parse_args()

# ----- CHAIN #1
llm = OpenAI()
prompt1 = PromptTemplate(template="Write a very short {language} function that {task}", input_variables=["language", "task"])
chain1 = LLMChain(llm=llm, prompt=prompt1, output_key="result1") # to change the default output key from "text" to "result1"



# ----- CHAIN #2
prompt2 = PromptTemplate(template="Write a very short test function for the following {language} code:\n {result1}", input_variables=["language", "result1"])
chain2 = LLMChain(llm=llm, prompt=prompt2, output_key="result2")

# ----- wiring the chains together
#listing out the chains one after another
# listing out the inputs
# listing out the outputs
chains = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["task", "language"],
    output_variables=["result1", "result2"]
)

result = chains({
    "language": args.language,
    "task": args.task
})

print(result)
