import re, string, operator, math

def clean_lyrics(s):
    s = remove_contributors(s)
    s = remove_lyrics_name(s)
    s = remove_embed(s)
    s = remove_song_structure(s)
    #s = remove_punctuation(s)
    return s
def remove_punctuation(s):
    no_punc = str.maketrans('', '', string.punctuation)
    return s.translate(no_punc)

def remove_contributors(s):
    s = re.sub(r'(\d+) Contributors', '', s)
    return s

def remove_lyrics_name(s):
    s = re.sub(r'.*?\ Lyrics', '', s)
    return s

def remove_embed(s):
    s = re.sub(r'—?\d+Embed', '', s)
    return s

def remove_song_structure(s):
    s = re.sub(r'\[(.*?)\]', '', s)
    return s

