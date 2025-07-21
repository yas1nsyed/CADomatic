# llm_client.py
import os
import google.generativeai as genai

# Configure API key from environment variable
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Set up the model
model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")

def prompt_llm(user_prompt: str) -> str:
    try:
        response = model.generate_content([
            "You are a helpful assistant that writes FreeCAD Python scripts from CAD instructions. Output only valid FreeCAD Python code, no extra text.",
            user_prompt
        ])
        return response.text
    except Exception as e:
        print("Error while generating FreeCAD code:", e)
        return ""
