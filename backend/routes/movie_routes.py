from flask import Blueprint, request, jsonify
from services.tmdb_service import search_movies

movie_bp = Blueprint("movies", __name__)

@movie_bp.route("/search")
def movie_search():
    query = request.args.get("q", "")
    if not query:
        return jsonify({"error": "Missing search query"}), 400

    results = search_movies(query)
    return jsonify(results)
