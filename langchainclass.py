from langchain_core.output_parsers import SimpleJsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

prompt=PromptTemplate.from_template(
    "In JASON format, give me list of {topic} and their"
    "corresponding names in french,spanish and in a"
    "Cat language"
)

model=ChatOllama(model="qwen2.5:3b")
chain=prompt | model | SimpleJsonOutputParser()

print(chain.invoke({"topic":"colors"}))