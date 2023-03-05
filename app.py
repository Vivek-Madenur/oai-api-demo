import os
from flask import Flask, render_template, request
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=1068,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
