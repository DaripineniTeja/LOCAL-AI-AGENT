from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriver

model = OllamaLLM(model="llama3.2")

template = """ 
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# ✅ Only run this if main.py is executed directly
if __name__ == "__main__":
    while True:
        print("\n\n-------------------------------------")
        question = input("Ask your question (q to quit): ")
        print("\n\n")

        if question.lower() == "q":
            break

        reviews = retriver.invoke(question)
        result = chain.invoke({"reviews": reviews, "question": question})
        print(result)
