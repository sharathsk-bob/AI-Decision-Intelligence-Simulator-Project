from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA

def analyze_decision(query, vector_store, api_key):
    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.1-8b-instant"
    )

    prompt = f"""
    You are a business strategy AI.
    Analyze this decision:
    {query}

    Provide:
    1. Similar historical cases
    2. Possible outcomes
    3. Risks involved
    4. Final recommendation
    """

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever()
    )

    return qa.run(prompt)
