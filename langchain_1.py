# importing the necessary libraries
import os
from dotenv import load_dotenv 
import langchain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Load the environment variables
load_dotenv()

# Get the OpenAI API key
openai_key = os.getenv("OPENAI_API_KEY")

# Create a new instance of the openai model
chat_gpt = ChatOpenAI(model = "gpt-4o-mini", temperature = 0)

# creating a prompt template
prompt = "Explain the {topic} in 2 bullet points."
template = ChatPromptTemplate.from_template(prompt)

# creating a chain
chain = (template
            |
         chat_gpt)

# collecting the response
response = chain.invoke({"topic" : "Generative AI"})

# printing the response
print(response.content)

# storing the output in a markdown file
with open("langchain_1.md", "w") as f:
    f.write(response.content)
