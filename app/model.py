import google.generativeai as genai
import json
from flask import jsonify, make_response
from utils.config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

def generate_response(data):
    """
    Sends order details to Gemini AI and converts them into structured JSON.
    """
    json_structure = data.get("jsonStructure")
    email_content = data.get("emailContent")

    prompt = f"""{email_content} 

Convert the above order details into the following structured JSON format:

{json.dumps(json_structure)}

Return the response **strictly** in JSON format, without explanations."""

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    print("response", response)

    structured_json = response.text.strip().replace("```json", "").strip().replace("```","").strip()

    print("Structured json", structured_json)

        # print("before structured json")
        # structured_json = json.loads(structured_json)
    return structured_json
