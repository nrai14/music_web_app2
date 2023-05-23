# EXAMPLE USER STORY:


As a music lover,
I want to update my records,
I want to able to create a new album. 

As a music lover,
So I keep track of my albums,
I want to see a list of all created albums. 

# EXAMPLE:

id: SERIAL
title: text
release_year: int
artist_id: int 


# WRITE THE SQL 

-- file: album_table.sql 

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int 
);


# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)


# TEST examples 
