from fastapi import FastAPI, Request, HTTPException
from typing import Optional
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from azure.cosmos import CosmosClient
import os
from dotenv import load_dotenv
import random

load_dotenv()


# Initialize FastAPI
app = FastAPI(
    title="Stoic Quotes API",
    summary="The very best Stoic quotes from the three great Roman Stoics: Marcus Aurelius, Seneca, and Epictetus.",
    version="0.0.1",
    contact={
        "name": "Rishab Kumar",
        "url": "http://rishabkumar.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/license/mit",
    },
)

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


templates = Jinja2Templates(directory="templates")

# Load Browser Favicon Icon
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/', description="Return the home page with a random quote.")
async def home(request: Request):
    """
    Return the home page with a random quote.

    - **request**: The request object.
    """
    random_document = random.choice(documents)
    random_quote = random.choice(random_document['quotes'])
    return templates.TemplateResponse('index.html', {"request": request, "quote": random_quote['quote'], "author": random_quote['author']})

@app.get('/api/random', description="Return a random quote.")
async def get_quote():
    """
    Return a random quote.

    This endpoint returns a random quote from the database in JSON format.
    """
    # Select a random document
    random_document = random.choice(documents)
    # Select a random quote from the 'quotes' array in the document
    random_quote = random.choice(random_document['quotes'])
    return {"quote": random_quote['quote'], "author": random_quote['author']}


@app.get('/api/search', description="Search for quotes containing a specific word.")
async def search(word: Optional[str] = None):
    """
    Search for quotes containing a specific word.

    - **word**: The word to search for in the quotes.

    This endpoint returns all quotes that contain the word in JSON format.
    """
    if not word:
        return HTTPException(status_code=400, detail="No word provided for search.")

    # Query for all documents
    documents = list(container.read_all_items())

    # Filter the quotes where the word appears
    matching_quotes = [quote for document in documents for quote in document['quotes'] if word.lower() in quote['quote'].lower()]

    if not matching_quotes:
        return {"response": 200, "message": "No quotes matched the query."}

    return {"response": 200, "results": matching_quotes}


# Build Pagination endpoint
@app.get('/api/quotes', description="Return a paginated list of quotes.")
async def pagination(page: Optional[int] = 1, limit: Optional[int] = 10):
    """
    Return a paginated list of quotes.

    - **page**: The page number to return.
    - **limit**: The number of quotes to return per page.

    This endpoint returns a paginated list of quotes in JSON format.
    """
    # Calculate the start and end index
    start_index = (page - 1) * limit
    end_index = page * limit

    # Query for all documents
    documents = list(container.read_all_items())

    # Extract all quotes from the documents
    all_quotes = [quote for document in documents for quote in document['quotes']]

    # Return the paginated list of quotes
    return {"response": 200, "results": all_quotes[start_index:end_index]}

if __name__ == '__main__':
    app.run()
