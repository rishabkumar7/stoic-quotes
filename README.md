# Stoic Quotes

[![Pytest](https://github.com/rishabkumar7/stoic-quotes/actions/workflows/run_test.yml/badge.svg)](https://github.com/rishabkumar7/stoic-quotes/actions/workflows/run_test.yml)


A simple Flask app that displays random Stoic quotes from stoics: Marcus Aurelius, Seneca and Epictetus.

## Using the API

This app also exposes a public API which you can use to fetch random Stoic quotes for use in your own applications.

### Endpoints

#### Get a random Stoic quote

```
GET https://stoic-qoutes.azurewebsites.net/api/random
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
GET https://stoic-qoutes.azurewebsites.net/api/<your_word>
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

## Author

- Twitter: [@rishabincloud](https://x.com/rishabincloud)
- GitHub: [@rishabkumar7](https://github.com/rishabkumar7)