# Single Table Design Recipe - 04.Test-Driving Route with Database: Chalenge

```
#USER STORY:


As a music lover,
So I can organise my records,
I want to keep a list of my favourite artists' names and genres.

As a music lover,
So I can organise my records,
I want to be able to add new artists' names and genres to this list.
```

```
Nouns:

artists, names, genres
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| artists               | name, genre         |

Name of the table (always plural): `artists`

Column names: `name`, `genre`

## 3. Decide the column types

```

id: SERIAL
name: text
genre: text
```

## 4. Write the SQL

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
  genre text
);


# Plain Route Design Recipe 04.Test-Driving Route with Database: Chalenge

## 1. Design the Route Signature

# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing

## 2. Create Examples as Tests

# GET /artists
#  Expected response (200 OK):
"""
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
"""

# POST /artists, data={'name': 'Wild Nothing', 'genre': 'Indie'}
#  Expected response (200 OK):
No content

## 3. Test-drive the Route

def test_get_all_artists(db_connection, web_client):
    db_connection.seed("seeds/artists_table.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "

def test_post_new_artist(db_connection, web_client):
    db_connection.seed("seeds/artists_table.sql")
    post_response = web_client.post('/artists', data={'name': '', 'genre': ''})
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-')








