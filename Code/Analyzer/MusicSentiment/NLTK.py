import io

import pandas as pd
from matplotlib import pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def vader_sentiment(track_name, artist, lyrics):
    #df = pd.DataFrame(columns=('artist', 'pos', 'neu', 'neg'))
    sid = SentimentIntensityAnalyzer()

    num_positive = 0
    num_negative = 0
    num_neutral = 0

    per_sentence_score = ''
    buf = io.StringIO(lyrics)
    for sentence in buf.readlines():
        score = sentence
        comp = sid.polarity_scores(sentence)
        comp = comp['compound']
        if comp >= 0.5:
            num_positive += 1
            score += ' (Positive)' + str(comp)
        elif -0.5 < comp < 0.5:
            score+=' (Neutral)' + str(comp)
            num_neutral += 1
        else:
            score += ' (Negative)' +str(comp)
            num_negative += 1
        score += '\n'
        per_sentence_score += score

        num_total = num_negative + num_neutral + num_positive
        percent_negative = (num_negative / float(num_total)) * 100
        percent_neutral = (num_neutral / float(num_total)) * 100
        percent_positive = (num_positive / float(num_total)) * 100
    print('Vader Sentiment:\nPercent positive: %3.2f \nPercent neutral: %3.2f \nPercent negative: %3.2f\n' % (percent_positive,percent_neutral,percent_negative))
    return('%s Percent positive: %3.2f \nPercent neutral: %3.2f \nPercent negative: %3.2f' % (per_sentence_score,percent_positive,percent_neutral,percent_negative))
