import json

import os
from pathlib import Path
import pandas as pd
from musixmatch import Musixmatch
musixmatch = Musixmatch('bc2fe5e01b680cd79b2d91754e066b88')

clear = lambda: os.system('cls')
root_dir = Path(__file__).resolve().parent.parent.parent.parent
print(root_dir)
test = musixmatch.chart_tracks_get(1,100,1, 'de', 'json')
track_list = test['message']['body']['track_list']
df = pd.json_normalize(track_list)

df.to_csv(root_dir / "Data" / "Charts" / "charts.csv")

list_wo_lyrics = df.loc[:,['track.track_id','track.track_name','track.artist_name']]
lyrics_array = []
print("gathering lyrics")
for i in range(len(list_wo_lyrics)):
    clear()
    print(i , ' of ' , len(list_wo_lyrics))

    lyrics_array.append(
        {
        'track_id': list_wo_lyrics['track.track_id'][i],
        'track_name': list_wo_lyrics['track.track_name'][i],
        'artist_name': list_wo_lyrics['track.artist_name'][i],
        'lyrics': musixmatch.track_lyrics_get(list_wo_lyrics['track.track_id'][i])['message']['body']['lyrics']['lyrics_body']
        }
    )

lyrics_df = pd.DataFrame(lyrics_array)
print(lyrics_df)
lyrics_df.to_csv(root_dir / "Data" / "Lyrics" / "lyrics.csv")