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
    header = ""
    introduction = ""

    if len(bot.conversation["prompts"]) == 0:
         header = bot.get_job_title_and_company(prompt)
         introduction = bot.converse(f"Introduce yourself as the interviewer of this job: {prompt}. Your name is Mr. Smith. Make up your job title. \
                                      Do not mention a company name if one is not provided")
         bot.conversation["prompts"].append(header)
         bot.conversation["answers"].append(introduction)
    else:
        bot.conversation["prompts"].append(prompt)
        bot.conversation["answers"].append(bot.converse(prompt))
        introduction = bot.conversation["answers"][0]
        header = bot.conversation["prompts"][0]


    return render_template('conversation.html', conversation = bot.conversation, header=header, introduction=introduction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
