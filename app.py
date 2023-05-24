from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
import os
from flask import Flask, request
from lib.album import Album

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

#Example:

@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

#Exercise:

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return "\n".join(
        f"{album}" for album in repository.all()
    )

@app.route('/albums', methods=['POST'])
def post_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        None, 
        request.form['title'],
        request.form['release_year'],
        request.form['artist_id'])
    repository.create(album)
    return '',200

#Challenge:













# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

