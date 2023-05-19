from flask import Flask, request, render_template, jsonify
#import nltk
from nltk import word_tokenize
#from custom_module import function1, function2  # custom python module
import logging
import datetime

logging.basicConfig(filename='conversation.log', level=logging.INFO)

#nltk.download('punkt')

app = Flask(__name__)

def process_text(text):
    tokens = word_tokenize(text)
    # Very basic intent processing
    if "greeting" in tokens:
        return "greeting"
    if "help" in tokens:
        return "help"
    else:
        return "unknown"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=['POST'])
def ask():
    question = request.json.get('question')
    
    intent = process_text(question)
    answer = ""

    # log the question, intent and answer
    log_data = {
        'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'question': question,
        'intent': intent,
        'answer': answer,
    }
    logging.info(str(log_data))
    
    # Depending on the intent, call different functions
    if intent == "greeting":
        return jsonify(answer="this is a test for greeting")  # from your custom python module
    elif intent == "help":
        return jsonify(answer="this is a test for help")  # from your custom python module
    else:
        return jsonify(answer="I'm not sure how to respond to that.")

if __name__ == "__main__":
    app.run(debug=True)
