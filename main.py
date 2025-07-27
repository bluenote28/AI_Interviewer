from flask import Flask, session
from flask import render_template, request
from ai_client import AiBot
from conversation import Conversation
from conversations import Conversations
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
bot = AiBot()

@app.route("/")
def main_page():

    if "all_conversations" in session:
    
        all_conversations = Conversations.from_dict(session['all_conversations'])

    else:
        all_conversations = []

    return render_template('index.html', conversations = all_conversations)

@app.route('/interview', methods=['POST'])
def interview():
    prompt = request.form['userprompt']
    

    if 'conversation' not in session:
        current_conversation = Conversation()
        current_conversation.header = bot.get_job_title_and_company(prompt)
        current_conversation.introduction = bot.converse(f"Introduce yourself as the interviewer of this job: {prompt}. Your name is Mr. Smith. Make up your job title. \
                                        Do not mention a company name if one is not provided")
        session['conversation'] = current_conversation.to_dict()

        if 'all_conversations' not in session:
            all_conversations = Conversations()
            session['all_conversations'] = all_conversations.to_dict()

        print(session['conversation'])
        
    else:
        current_conversation = Conversation.from_dict(session['conversation'])
        current_conversation.conversation["prompts"].append(prompt)
        current_conversation.conversation["answers"].append(bot.converse(prompt))
        session['conversation'] = current_conversation.to_dict()
        print(session['conversation'])
        
    return render_template('conversation.html', conversation = current_conversation.conversation, header=current_conversation.header, introduction=current_conversation.introduction)


@app.route('/end_conversation', methods=['POST'])
def end_conversation():
    print(session['conversation'])
    conversation = Conversation.from_dict(session['conversation'])
    all_conversations = Conversations.from_dict(session['all_conversations'])
    all_conversations.conversations.append(conversation)
    session['all_conversations'] = all_conversations.to_dict()
    session.pop('conversation', None)

    return render_template('index.html', conversations=all_conversations.conversations)


@app.route('/interview/<header>', methods=['GET'])
def specific_interview(header):

    all_conversations = Conversations.from_dict(session['all_conversations'])

    selected_conversation = None

    for conversation in all_conversations.conversations:
        if conversation.header == header:
            selected_conversation = conversation

    session['conversation'] = selected_conversation.to_dict()
    
    return render_template('conversation.html', conversation=selected_conversation.conversation, 
                           header=selected_conversation.header, introduction=selected_conversation.introduction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
