import requests
from config.config import *

def get_weather(city: str) -> str:
    """
    Retrieves the current weather status for a given city.
    
    :param city: The name of the city for which to retrieve the weather status.
    """
    params = {
        'q': city,
        'appid': OPENWEATHERMAP_API_KEY,
        'units': 'metric'  # Change to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)
        response.raise_for_status()  # Raise an error for bad responses

        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']

        w = f"The current weather in {city} is {weather_description} with a temperature of {temperature}°C."
        return w

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"
    
def get_news(query: str) -> str:
    """
    Retrieves news articles based on a search query.
    
    :param query: The keyword or phrase to search for in the news articles.
    """
    params = {
        'q': query,
        'apiKey': NEWSAPI_API_KEY,
        'pageSize': 5,  # Number of articles to retrieve
        'language': 'en'  # Language of the articles
    }

    try:
        response = requests.get('https://newsapi.org/v2/everything', params=params)
        response.raise_for_status()  # Raise an error for bad responses

        data = response.json()

        if data['status'] == 'ok' and data['totalResults'] > 0:
            articles = data['articles']
            news_items = []
            for article in articles:
                title = article['title']
                description = article['description']
                news_items.append(f"Title: {title}\nDescription: {description}\n")

            return "\n- ".join(news_items)
        else:
            return "No news articles found."

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"
