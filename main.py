from flask import Flask
from flask import render_template, request
from ai_client import AiBot

app = Flask(__name__)
bot = AiBot()

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route('/interview', methods=['POST'])
def interview():
    prompt = request.form['userprompt']

    bot.conversation["prompts"].append(prompt)
    bot.conversation["answers"].append(bot.call_gemini(prompt))

    return render_template('conversation.html', conversation = bot.conversation)
