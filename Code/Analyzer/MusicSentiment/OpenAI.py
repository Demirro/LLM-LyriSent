from os import environ

from openai import OpenAI

client = OpenAI()
from openai import OpenAI

client = OpenAI()


def check_sentiment_openai(song):
    lyrics = song['lyrics']
    # Example OpenAI Python library request
    MODEL = "gpt-4"
    response = client.chat.completions.create(model=MODEL,
                                              messages=[
                                                  {"role": "system",
                                                   "content": "You are a machine that analyzes the sentiment of any given song lyrics fed to you by the user. You give a score between -1.0 (negative) and +1.0 (positive) for each sentence of the lyrics. A sentence is to be negative between -1.0 and -0.5, neutral between -0.5 and 0.5, positive between 0.5 and 1.0.You then are to simply output a percentage for overall positive sentiment, neutral sentiment and negative sentiment based on the number of positive, neutral and negative sentences in the song. The output should for the sentences should look like (remove the [] brackets when filling it in): '[Sentence here] (sentiment either Positive, Neutral or Negative) [Sentiment Score]. The output for the overall score should look like the following format:\nPercent positive: 14.29\nPercent neutral: 77.55\nPercent negative: 8.16. "},
                                                  {"role": "user",
                                                   "content": "Analyze the following lyrics: \n" + lyrics},
                                              ],
                                              temperature=0)
    return response.choices[0].message.content
