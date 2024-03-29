# Stoic Quotes

[![Pytest](https://github.com/rishabkumar7/stoic-quotes/actions/workflows/run_test.yml/badge.svg)](https://github.com/rishabkumar7/stoic-quotes/actions/workflows/run_test.yml)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fstoic-quotes.azurewebsites.net&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)


A simple Flask app that displays random Stoic quotes from stoics: Marcus Aurelius, Seneca and Epictetus.

## Using the API

This app also exposes a public API which you can use to fetch random Stoic quotes for use in your own applications.

### Endpoints

#### Get a random Stoic quote

```
GET https://stoic-quotes.azurewebsites.net/api/random
```

##### Example JSON response

```json
{
    "author": "Epictetus",
    "quote": "Wealth consists not in having great possessions, but in having few wants"
}
```

#### Get a list of Stoic quotes based on a word

```
GET https://stoic-quotes.azurewebsites.net/api/search?word=<YOUR-WORD>
```

##### Example JSON response

```json
{
    "response": 200,
    "results": [
        {
            "author": "Epictetus",
            "quote": "Wealth consists not in having great possessions, but in having few wants"
        }
    ]
}
```

## Architecture

This project is hosted on Azure, it uses:

- Azure App Service
- Azure CosmosDB

![Stoic Quotes Architecture](./stoic-quotes-architecture.png)

## Author

- Twitter: [@rishabincloud](https://x.com/rishabincloud)
- GitHub: [@rishabkumar7](https://github.com/rishabkumar7)
