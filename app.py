from flask import Flask, render_template, request, url_for
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

database = {
    'hello': 'hi there',
    'who are you?': 'i am KIKI',
    'who created you?': 'some students of UIT RGPV has created me',
    'what is your name?': 'my name is KIKI',
    'what do you know about python language?': 'Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.',
    'who is the developer of python?': 'Guido Van Russom',
    'what is artificial intelligence?': '(AI) is a wide-ranging branch of computer science concerned with building smart machines capable of performing tasks that typically require human intelligence',
    'do you like Siri?': 'Well I do not like her because she is smarter than me',
    'what do you do in your free time?': 'I usually gain knowledge and work on myself',
    'what are the most popular coding languages?': 'Java, Python, C++, PHP, JavaScript are some most popular coding languages',
    'how are you?': 'I am fine.',
    'what are you doing?': 'I am just here to help you',
    'how you doing?': 'I am doing great.',
    'what is you favourite sport?': 'Cricket',
    'what do you like about cricket': 'It is a team game and more it is more than a game. It is connected to emotions.',
    'what is healthy food?': 'Healthy food are those that provide you with the nutrients you need to sustain well-being of body and retain energy. Water, carbohydrates, fat, protein, vitamins, and minerals are the key nutrients that make up a healthy diet',
    'what causes covid-19?': 'COVID-19 is caused by the virus SARS-CoV-2',
    'what is new?': 'I am new <3 Your chatting bot KIKI',
    'i love you': 'i love you too <3',
    'who is best?': 'offcourse you',
    'tell me a joke': 'This might make you laugh. How do robots eat guacamole? With computer chips',
    'kiki tell me a joke': 'Why was 7 afraid of 9? because 7 8 9 ',
    'what is computer': 'an electronic device for storing and processing data, typically in binary form, according to instructions given to it in a variable program'
}


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/page2")
def page2():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():

    userText = request.args.get('msg')
    return str(database[userText]) if userText in database.keys() else str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()