from lib.artist import Artist 


def test_artist_constructs():
    artist = Artist(1, "Test Name", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Name"
    assert artist.genre == "Test Genre"


def test_artist_format_nicely():
    artist = Artist(1, "Test Name", "Test Genre")
    assert str(artist) == "Artist(1, Test Name, Test Genre)"


def test_artists_are_equal():
    artist1 = Artist(1, "Test Name", "Test Genre")
    artist2 = Artist(1, "Test Name", "Test Genre")
    assert artist1 == artist2


    