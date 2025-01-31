import google.generativeai as genai
import json
from config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

def generate_response(data):
    """
    Sends order details to Gemini AI and converts them into structured JSON.
    """
    prompt = f"""{json.dumps(data)} 

Convert the above order details into the following structured JSON format:

{{
  "order": {{
    "id": "String",
    "state": "String",
    "billing": {{
      "name": "String",
      "phone": "String",
      "email": "String"
    }},
    "items": [
      {{
        "id": "String",
        "name": "String",
        "quantity": "Number"
      }}
    ]
  }}
}}

Return the response **strictly** in JSON format, without explanations."""

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    structured_json = response.text.strip().replace("```json", "").replace("```", "").strip()
    return structured_json
