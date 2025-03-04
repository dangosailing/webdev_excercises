from flask import Flask, request, render_template
from config import BASE_URL, API_KEY
import requests

app = Flask(__name__)


@app.route("/")
def index():
    headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
    }

    params = {
    'query': 'Godfather'
    }   

    response = requests.request("GET", url=f"{BASE_URL}/search/movie", headers=headers, params=params).json()
    results = response["results"]
    return render_template("index.html", results=results)

@app.route("/search", methods=["GET", "POST"])
def search_movies():
    headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
    }

    params = {
    'query': request.form.get("search")
    }   

    response = requests.request("GET", url=f"{BASE_URL}/search/movie", headers=headers, params=params).json()
    results = response["results"]
    return render_template("index.html", results=results)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)