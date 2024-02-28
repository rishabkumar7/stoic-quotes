from flask import Flask, jsonify, render_template, request
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

@app.route('/api/random', methods=['GET'])
def get_quote():
    random_quote = random.choice(quotes)
    return jsonify(random_quote), 200


@app.route('/api/search/<word>', methods=['GET'])
def search(word):
    matching_quotes = [quote for quote in quotes if word.lower() in quote['quote'].lower()]
    if not matching_quotes:
        return jsonify({'response': 200, 'message': 'No quotes matched the query.'})
    return jsonify({'response': 200, 'results': matching_quotes})


@app.route('/api/word', methods=['POST'])
def word():
    data = request.get_json()
    word = data.get('word', '')
    matching_quotes = [quote for quote in quotes if word.lower() in quote['quote'].lower()]
    if not matching_quotes:
        return jsonify({'response': 200, 'message': 'No quotes matched the query.'})
    return jsonify({'response': 200, 'results': matching_quotes})


if __name__ == '__main__':
    app.run()
