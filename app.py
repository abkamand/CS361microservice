from flask import Flask, json, jsonify, request, render_template
import requests


app = Flask(__name__)


@app.route("/")
def home():
    return "<h1> test home </h1>"


# transform youtube video id into a youtube embed link and return
@app.route("/embedlink")
def embed_link():
    video_id = request.args.get('videoid')
    embed_link = "https://www.youtube.com/embed/" + video_id

    return embed_link


# Listener
if __name__ == "__main__":
    #Start the app on port 3000, it will be different once hosted
    app.run(port=65334, debug=True)
