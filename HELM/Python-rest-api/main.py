from flask import Flask, render_template

app = Flask(__name__)

# Sample data for anime list
anime_list = [
    {"id": 1, "title": "Fullmetal Alchemist: Brotherhood", "year": 2009, "genre": "Action, Adventure, Fantasy"},
    {"id": 2, "title": "Attack on Titan", "year": 2013, "genre": "Action, Drama, Fantasy"},
    {"id": 3, "title": "Naruto: Shippuden", "year": 2007, "genre": "Action, Adventure, Drama"},
    {"id": 4, "title": "Death Note", "year": 2006, "genre": "Mystery, Thriller, Supernatural"},
    {"id": 5, "title": "My Hero Academia", "year": 2016, "genre": "Action, Comedy, Superhero"},
    {"id": 6, "title": "One Piece", "year": 1999, "genre": "Action, Adventure, Comedy"},
    {"id": 7, "title": "Steins;Gate", "year": 2011, "genre": "Sci-Fi, Thriller"},
    {"id": 8, "title": "Demon Slayer: Kimetsu no Yaiba", "year": 2019, "genre": "Action, Fantasy, Supernatural"},
    {"id": 9, "title": "Your Name", "year": 2016, "genre": "Drama, Romance, Supernatural"},
    {"id": 10, "title": "Cowboy Bebop", "year": 1998, "genre": "Action, Adventure, Sci-Fi"}
]

@app.route('/')
def index():
    return render_template('index.html', anime=anime_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)
