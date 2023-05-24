# Tests for your routes go here

# Example:
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

#Exercise:

def test_get_all_album(db_connection, web_client):
    db_connection.seed("seeds/album_table.sql")
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Album(1, Hypnotised, 1980, 1)"

def test_post_new_album(db_connection, web_client):
    db_connection.seed("seeds/album_table.sql")
    post_response = web_client.post('/albums', data={'title': 'Voyage', 'release_year': '2022', 'artist_id': '2'})
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-')


#Challenge:
#     

def test_get_all_artist(db_connection, web_client):
    db_connection.seed("seeds/artist_table.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Artist(1, Pixies, Indie)\nArtist(2, ABBA, Pop)\nArtist(3, Taylor Swift, Country)\nArtist(4, Nina Simone, Jazz)" 
        

def test_create_new_artist(db_connection, web_client):
    db_connection.seed("seeds/artist_table.sql")
    post_response = web_client.post('/artists', data={'name': 'Wild Nothing', 'genre': 'Indie'})
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-')