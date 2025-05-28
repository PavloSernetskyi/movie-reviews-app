import os
import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_API_URL = "https://api.themoviedb.org/3"

def search_movies(query):
    response = requests.get(
        f"{TMDB_API_URL}/search/movie",
        params={
            "api_key": TMDB_API_KEY,
            "query": query,
        }
    )
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"TMDb Error: {response.status_code} {response.text}")
        return []
