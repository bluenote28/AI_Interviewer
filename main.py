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

    if len(bot.conversation["prompts"]) == 0:
         header = AiBot.summarize_text(prompt)
         introduction = bot.converse(f"Introduce yourself as the interviewer of this job: {prompt}")
    else:
        bot.conversation["prompts"].append(prompt)
        bot.conversation["answers"].append(bot.converse(prompt))


    return render_template('conversation.html', conversation = bot.conversation, header=header, introduction=introduction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
