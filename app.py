from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

app = Flask(__name__)

# Configure Google Generative AI
genai.configure(api_key=google_api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_text():
    data = request.get_json()
    input_text = data['text']

    try:
        # Generate code using gemini-1.5-flash
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(input_text)
        code = response.text

        # Format the code (if it's JSON)
        try:
            formatted_code = json.dumps(json.loads(code), indent=4) #Format json code
        except json.JSONDecodeError:
            formatted_code = code # If it's not JSON, use the raw code.

        # Wrap in HTML <pre> and <code> tags
        html_code = f'<pre><code>{formatted_code}</code></pre>'

        result_text = html_code

    except Exception as e:
        result_text = f"Error generating code: {e}"

    return jsonify({'result': result_text})

if __name__ == '__main__':
    app.run(debug=True)