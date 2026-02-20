from flask import Flask, session, redirect, url_for
from flask import render_template, request, jsonify
from ai_client import AiBot
from conversation import Conversation
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
bot = AiBot()

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route('/interview', methods=['POST'])
def interview():
    prompt = request.form['userprompt']
    
    if prompt == "":
        return redirect(url_for('main_page'))

    if 'conversation' not in session and bot.is_job_description(prompt) == 'no':
        return render_template('error.html', error="The text you entered does not appear to be a job description. Please enter a valid job description to start the interview.")

    if 'conversation' not in session:
        current_conversation = Conversation()
        try: 
            current_conversation.header = bot.get_job_title_and_company(prompt)
            current_conversation.introduction = bot.converse(f"Introduce yourself as the interviewer of this job: {prompt}. Your name is Mr. Smith. Make up your job title. \
                                        Do not mention a company name if one is not provided. Make sure to include the first question of the interview")
        except Exception as e:
            return render_template('error.html', error=str(e))

        session['conversation'] = current_conversation.to_dict()
   
    else:

        try: 
            current_conversation = Conversation.from_dict(session['conversation'])
            current_conversation.conversation["prompts"].append(prompt)
            current_conversation.conversation["answers"].append(bot.converse(prompt))
            session['conversation'] = current_conversation.to_dict()
        except Exception as e:
            return render_template('error.html', error=str(e))
        
    return render_template('conversation.html', conversation = current_conversation.conversation, header=current_conversation.header, introduction=current_conversation.introduction)


@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.get_json()
    prompt = data.get('prompt', '').strip()

    if not prompt:
        return jsonify({'error': 'Empty prompt'}), 400

    if 'conversation' not in session:
        return jsonify({'error': 'No active conversation'}), 400

    current_conversation = Conversation.from_dict(session['conversation'])

    try:
        answer = bot.converse(prompt)
        current_conversation.conversation["prompts"].append(prompt)
        current_conversation.conversation["answers"].append(answer)
        session['conversation'] = current_conversation.to_dict()

        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)