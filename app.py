from flask import Flask, render_template, request
from dotenv import load_dotenv
import google.generativeai as genai
import openai
import os
import json

#to load env 
load_dotenv()
app = Flask(__name__)

# config gemini and open ai
MODEL_TYPE = os.getenv("MODEL_TYPE", "gemini")  # gemini/openai

if MODEL_TYPE == "gemini":
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("models/gemini-2.5-flash")
elif MODEL_TYPE == "openai":
    openai.api_key = os.getenv("OPENAI_API_KEY")


# adding routes
@app.route('/')
def home():
    return render_template('index.html')

#user prompt to make sure each slide contain only one specific info and receives info in json format

@app.route('/generate', methods=['POST'])
def generate_presentation():
    user_text = request.form.get('input_text')

    prompt = f"""
    Summarize this into 6 concise slides in pure JSON:
    [{{"title": "...", "content": "..."}}]
    Input:
    {user_text}
    """

    if MODEL_TYPE == "gemini":
        response = model.generate_content(prompt)
        text = response.text
    elif MODEL_TYPE == "openai":
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        text = response.choices[0].message["content"]

    # to Parse slides safely
    try:
        json_start = text.find('[')
        json_end = text.rfind(']')
        slides = json.loads(text[json_start:json_end + 1])
    except Exception as e:
        slides = [{"title": "Error", "content": f"Could not parse slides: {str(e)}"}]

    return render_template("result.html", slides=slides, input_text=user_text)

# run prgm

if __name__ == "__main__":
    app.run(debug=True)
