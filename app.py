from flask import Flask, jsonify, render_template, request
import random
import json
from azure.cosmos import CosmosClient
import os
from dotenv import load_dotenv

load_dotenv()


#Initialize Flask
app = Flask(__name__)

# Initialize Cosmos Client
url = os.getenv("AZURE_COSMOSDB_URL")
key = os.getenv("AZURE_COSMOSDB_KEY")
client = CosmosClient(url, credential=key)

# Select database
database_name = 'Quotes'
database = client.get_database_client(database_name)

# Select container
container_name = 'stoic-quotes'
container = database.get_container_client(container_name)

# Query for all documents
documents = list(container.read_all_items())


@app.route('/')
def home():
    random_document = random.choice(documents)
    random_quote = random.choice(random_document['quotes'])
    return render_template('index.html', quote=random_quote['quote'], author=random_quote['author'])

@app.route('/api/random', methods=['GET'])
def get_quote():
    # Select a random document
    random_document = random.choice(documents)
    # Select a random quote from the 'quotes' array in the document
    random_quote = random.choice(random_document['quotes'])
    return jsonify(random_quote), 200


@app.route('/api/search', methods=['GET'])
def search():
    word = request.args.get('word', '')
    if not word:
        return jsonify({'response': 200, 'message': 'No word provided for search.'})

    # Query for all documents
    documents = list(container.read_all_items())

    # Filter the quotes where the word appears
    matching_quotes = [quote for document in documents for quote in document['quotes'] if word.lower() in quote['quote'].lower()]

    if not matching_quotes:
        return jsonify({'response': 200, 'message': 'No quotes matched the query.'})

    return jsonify({'response': 200, 'results': matching_quotes})


#Build Pagination endpoint

if __name__ == '__main__':
    app.run()
