import os
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

src_path = os.path.dirname(os.path.abspath(__file__))
root_dir_path = os.path.dirname(src_path)
vectorstore_path = os.path.join(root_dir_path, "vectorstore")

# Load the vectorstore and retriever
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = FAISS.load_local(vectorstore_path, embedding, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_kwargs={"k": 20})

# Load Gemini 2.5 Flash model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.2)

def prompt_llm(user_prompt: str) -> str:
    docs = retriever.invoke(user_prompt)
    context = "\n\n".join(doc.page_content for doc in docs)

    final_prompt = f"""
You are a helpful assistant that writes FreeCAD Python scripts from CAD instructions.
Use the following FreeCAD wiki documentation as context:

{context}

Instruction:
{user_prompt}

Respond with valid FreeCAD Python code only, no extra commentary.
"""

    try:
        response = llm.invoke(final_prompt)
        return response.content
    except Exception as e:
        print("❌ Error generating FreeCAD code:", e)
        return ""
