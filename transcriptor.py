from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
import nltk
from string_conversion import modify_transcript,get_string_format
app = Flask(__name__)
nltk.download("vader_lexicon")
nltk.download("punkt")


@app.route("/get_transcript/<videoID>", methods=["GET"])
def get_transcript(videoID):
    json_list = YouTubeTranscriptApi.get_transcript(videoID, languages=["en", "en-US"])
    string_format = get_string_format(json_list)
    transcript = modify_transcript(60, 6000, videoID, string_format)
    return {"txt": transcript.lower()}


if __name__ == '__main__':
    app.run(debug=True)
