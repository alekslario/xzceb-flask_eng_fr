import json
from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator", template_folder='templates')

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(textToTranslate)

@app.route("/")
def render_index_page():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
