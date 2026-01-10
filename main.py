from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm_openai = ChatOpenAI(model="gpt-4.1-nano", temperature=0)
llm_google = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

m1 = "Who is the Prime Minister of India?"

response_openai = llm_openai.invoke(m1)
response_google = llm_google.invoke(m1)
print("question:", m1)
print("OpenAI Response:", response_openai.content)
print("Google Generative AI Response:", response_google.content)

m2 = "What is his age?"
response_openai = llm_openai.invoke(m2)
response_google = llm_google.invoke(m2)
print("question:", m2)
print("OpenAI Response:", response_openai.content)
print("Google Generative AI Response:", response_google.content)