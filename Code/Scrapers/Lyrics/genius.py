from lyricsgenius import Genius

token = ''

# this gets the lyrics of all the songs that have the pop tag.
genius = Genius(token, timeout=5, retries=3, response_format='plain,html')
genius.response_format='html'
# page = 1
# lyrics = []
# while page<2:
#     print(page)
#     res = genius.tag('pop', page=page)
#     for hit in res['hits']:
#         song_lyrics = genius.lyrics(song_url=hit['url'])
#         lyrics.append(song_lyrics)
#     page = res['next_page']
#
# print(lyrics)

# STRING STUFF

def fetch_lyrics(artist_name, track_name):
    try:
        # Search for the song on Genius
        song = genius.search_song(track_name, artist_name)
        if song is not None:
            return {
                'artist': artist_name,
                'track': track_name,
                'lyrics': song.lyrics
            }
        else:
            print(f"Lyrics not found for {artist_name} - {track_name}")
            return None
    except Exception as e:
        print(f"Error fetching lyrics for {artist_name} - {track_name}: {e}")
        return None

