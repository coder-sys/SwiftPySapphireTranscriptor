from flask import Flask, render_template, request,jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import nltk
from string_conversion import modify_transcript,get_string_format,sent_tokenize,tokenize_string
from youtubesearchpython import VideosSearch

app = Flask(__name__)
nltk.download("vader_lexicon")
nltk.download("punkt")

@app.route("/get_transcript/<query>", methods=["GET"]) 
def get_transcript(query):
    limit = 10
    videos_search = VideosSearch(query, limit=limit)  # Limit the search results to 20 videos

    thumbnails = []
    sentTokens = []
    tokens = []
    names = []
    links = []
    transcripts = []
    scores = []
    for video in videos_search.result()['result']:
        try:
            json_list = YouTubeTranscriptApi.get_transcript(video["id"], languages=["en", "en-US"])
            print(video["id"])
            thumbnails.append(video['thumbnails'][0]["url"])
            names.append(video['title'])
            links.append('https://www.youtube.com/watch?v=' + video['id'])
            string_format = get_string_format(json_list)
            transcript = modify_transcript(180, 6000, video["id"], string_format)
            transcripts.append(transcript.lower())
            tokens.append(tokenize_string(transcript.lower()))
            sentTokens.append(sent_tokenize(transcript.lower()))
            scores.append(float(1/limit))

        except:
            continue
    print(thumbnails[0],names[0],tokens[0])
    return {"thumbnails": thumbnails,"sentTokens":sentTokens,"tokens":tokens , "links": links, "names": names, "transcripts": transcripts,"scores":scores}

"""
@app.route("/get_transcript/<query>", methods=["GET"])
def get_transcript(query):
    return {
        "txt":query
    }
"""

if __name__ == '__main__':
    app.run(debug=True)
