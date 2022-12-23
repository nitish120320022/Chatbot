from flask import Flask, render_template, request
import nltk
from nltk.chat.util import Chat
app = Flask(__name__)
qa_pairs = [ ['(.*)name', ['I am Ultron']],
            ['(hi|Hi|hey|Hey|hello|Hello)', ['Hey, Ultron is here.']], ['How are you', ['I am fine, What about you?']],
            ['(.*)location|city|address?', ['Address: Poornima institute of engineering and technology, Sitapura, Jsipur']],
            ['(.*)contact(.*)', ['9509937238']], ['(.*)weather(.*)', ['It is too hot']], 
            ['What is your favourite movie', ['John wick']] ]
cb = Chat(qa_pairs)
@app.route('/', methods = ['GET','POST'])
def chatbot_response():
    response = ' '
    if request.method == 'POST':
        msg = request.form['message']
        response = cb.respond(msg)
    return render_template('index.html', response1 = response)

if __name__ == '__main__':
    app.run(debug = True)
