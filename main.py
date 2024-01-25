import csv
import json
import os.path

from Code.PreProcessing.LyricsCleanUp import clean_lyrics
from Code.Scrapers.Lyrics.genius import fetch_lyrics
from Code.Analyzer.MusicSentiment.OpenAI import check_sentiment_openai
from Code.Analyzer.MusicSentiment.NLTK import vader_sentiment

json_file_path = 'Data/Lyrics/Prompt4/gpt4/songs_data.json'
try:
    existingJson = json.load(open(json_file_path, encoding='utf8'))
except FileNotFoundError:
    existingJson = []

checked_track = dict()
def is_track_checked(track_to_check):
    global checked_track
    if existingJson:
        for track in existingJson:
            if track and track['track'].casefold() == track_to_check.casefold():
                print(track['track'] + ' was already checked. It was skipped')
                checked_track = track
                return True
def has_gpt_response(track_to_check):
    for track in existingJson:
        if track['track'].casefold() == track_to_check.casefold():
            if track['gpt_response'] != '':
                return True
def _input(message, input_type=str):
    while True:
        try:
            return input_type(input(message))
        except:pass
def main():
    # List of songs (artist, track)
    songs_list = [
    ]
    prefab_check = input('Do you want to use the prefab list of songs (10 songs)? Yes (y/Y) or No (n/N)\n')
    if prefab_check.casefold() in {'yes','y'}:
        songs_list = [
            ('Childish Gambino','This is America'),
            ('brakence','deepfacke'),
            ('Peter Fox','Haus am See'),
            ('Feu! Chatterton', "J'ai tout mon temps"),
            ('Bruno Mars', 'Treasure'),
            ('Ed Sheeran', 'Shape Of You'),
            ('The Japanese House', 'Saw You In A Dream'),
            ('Tom Misch', 'Disco Yes'),
            ('Radiohead', 'Creep'),
            ('Jacob Collier', 'Hideaway'),
        ]
    elif prefab_check.casefold() in {'no','n'}:
        number_of_songs = _input('How many songs do you want to check: ', int)
        for i in range(number_of_songs):
            print('Song no. ' + str(i+1))
            track_name = input('Track Name: ')
            artist = input('Artist: ')
            songs_list.append((artist, track_name))
            print('\n')
        print(songs_list)
    else:
        print('Yes (y/Y) or No (n/N)')
    # Fetch lyrics for each song
    data = []
    for artist, track in songs_list:
        if not is_track_checked(track):
            result = fetch_lyrics(artist, track)
            if result:
                lyrics = result['lyrics'] = clean_lyrics(result['lyrics'])
                if not has_gpt_response(track):
                    result['gpt_response'] = check_sentiment_openai(result)
                result['vader_sentiment'] = vader_sentiment(track, artist,lyrics)
                data.append(result)
    existingJson.extend(data)

    # # Save the data as CSV
    # csv_file_path = 'Data/Lyrics/songs_data.csv'
    # with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    #     fieldnames = ['artist', 'track', 'lyrics', 'gpt_response']
    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     writer.writeheader()
    #     writer.writerows(data)

    # Save the data as JSON
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(existingJson, json_file, ensure_ascii=False, indent=4)


    print(f"Data has been saved to {json_file_path}")

if __name__ == "__main__":
    main()