from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm_openai = ChatOpenAI(model="gpt-4.1-nano", temperature=1, max_tokens=100) #initializing the openai model
# Temperature - controls the randomness of the model's output
# max temperature - 1.0 (most random)
# min temperature - 0.0 (least random)
# max tokens - controls the maximum number of tokens in the response
# min tokens - controls the minimum number of tokens in the response
llm_google = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1) #initializing the google model

m1 = "Who is the Prime Minister of India?" #first question

response_openai = llm_openai.invoke(m1) #calling the openai model
response_google = llm_google.invoke(m1) #calling the google model
print("question:", m1) #printing the question
print("OpenAI Response:", response_openai.content) #printing the openai response
print("Google Generative AI Response:", response_google.content) #printing the google response

m2 = "What is his age?"
response_openai = llm_openai.invoke(m2)
response_google = llm_google.invoke(m2)
print("question:", m2)
print("OpenAI Response:", response_openai.content)
print("Google Generative AI Response:", response_google.content)
# example response
print("Example response Google :")
print(response_google)
print("Example response OpenAI :")
print(response_openai)