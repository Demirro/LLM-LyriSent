# LLM-LyriSent
Experimental annotation of sentiment of musical lyrics by a LLM - WS23/24 Annotation mit Sprachmodellen

## Intro
Music and song lyrics are intended to convey and trigger certain feelings. Although the perception of music is always different, there are metrics and evaluations of the so-called sentiment of songs. Similar to literary texts, reviews or other written artifacts, song lyrics themselves are often analyzed and certain words are used to evaluate how positive or negative the corresponding text and song is.


> This project is a student project for the course [Annotation mit Sprachmodellen](https://lehre.idh.uni-koeln.de/lehrveranstaltungen/wintersemester-2023-2024/sprachmodelle-1/) at the Institute for Digital Humanities at the University of Cologne

## Goal
This experiment aims to test the waters of automatic sentiment annotation of musical lyrics by using LLM. Specifically I want to test the capability of (mainly) GPT to recognize sentiment in lyrics and also test if it can recognizes changes of sentiment across a song and across time (development of sentiment in charts over time and possibly related to specific events). This would potentially improve annotation time and make music analysis simpler, especially when coupled with already existing tools and musical sentiment analysis (e.g. Spotify).

## Experiment
### 1. Questions I want answers to (the questions is always aimed at lyrics, not other musical content):
- Is the entire song positive, negative or neutral?
  - Could there be finer steps of sentiment or more nuanced emotional categories (e.g. happy, melancholy, angry)
- Does the sentiment change throughout the song?
  - Does it get more positive, negative or neutral?
  - How does it change?
  - How fine can the subdivisions be (e.g. verses, lines of lyrics, sentences)
- Which tokens and sentences does the LLM consider most impactful? (e.g. "explicit" language, negative words like "crying/weeping/missing", positive words like "sunshine, smile, happy")
- Does the lyrical sentiment consistently relate to the music sentiment?
### 2. Data I want and will have to use:
- The music catalog (lyrics) of a handful of artists (English) from a genre (preferably pop or rock). For example, the pop charts in January 2020
  - Already scraped chart data possibly from [mhollingshead](https://github.com/mhollingshead/billboard-hot-100)
  - Lyrics will be taken from [MusixMatch](https://developer.musixmatch.com/) or [Genius](https://docs.genius.com/) --> Whichever is easiest to work with
- Depending on the result and effort, the experiment can be extended to other genres and artists
- For comparison: Sentiment score from the [Spotify API](https://developer.spotify.com/documentation/web-api) and other sentiment data sets such as [AFINN](https://darenr.github.io/afinn/)
### 3. LLM I will use:
- GPT 3.5
- possibly GPT 4 to compare
- First I will test it with ChatGPT and might look into the OpenAI API
### 4. Experiment Design (First Draft):
- Get all the data
- Clean it up, store it and prepare it for automatic use
- Try different annotating the texts by using a LLM
  - Zero Shot Prompting:
    - Give the LLM the lyrics and ask different kind of questions about the sentiment (see 1)
    - Store all the prompts and result
  - Few Shot Prompting:
    - Give the LLM different kind of examples of what I want the output to look like (roughly) including sentiment scores
    - Store all the prompts and results
  - Let it correct already annotated data (could probably only be a small set of lyrical data)
  - Finetuning (probably out of scope for this course)
- Compare all the results with known good sentiment analysis of the given texts and a handful of manual annotations
