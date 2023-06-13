from flask import Flask, jsonify, render_template
import random
import json

app = Flask(__name__)

# Load the quotes from the JSON file
with open('data/quotes.json', 'r') as f:
    quotes = json.load(f)['quotes']

@app.route('/')
def home():
    random_quote = random.choice(quotes)
    return render_template('index.html', quote=random_quote['quote'], author=random_quote['author'])

@app.route('/api/quote', methods=['GET'])
def get_quote():
    random_quote = random.choice(quotes)
    return jsonify(random_quote)

if __name__ == '__main__':
    app.run()
