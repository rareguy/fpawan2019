from flask import Flask, request
from flask.json import jsonify
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return 'Server Works!'
  
@app.route('/ytdownload', methods=["POST"])
def say_hello():
    req_data = request.get_json()
    if "youtube_link" in req_data:
        yt_object = YouTube(req_data["youtube_link"])
        stream = yt_object.streams.all()
        for i in stream:
            print(i)
        # kalo cuman bilang link video saja
        if "format" not in req_data:
            all_stream = get_all_stream(stream)
            req_response = {
                "status": "OK",
                "availability": "ready to download, pick your codec with number ID",
                "youtube_link": req_data["youtube_link"],
                "title": yt_object.title,
                "views": yt_object.views,
                "codec": all_stream
                }
        else:
            # TODO: cari formatan video di tiap stream, terus di"konfirmasi" kalo mau pilih format itu
            req_response = {
                "status": "OK",
                "availability": "format picked",
                "youtube_link": req_data["youtube_link"],
                "title": yt_object.title,
                "views": yt_object.views,
                "codec": all_stream
                }
            
        return jsonify(req_response), 200
    return jsonify(error_dictionary("sowwy :("))

def error_dictionary(message):
    x = {
        "status": "ERROR",
        "message": message
        }
    return x

def get_all_stream(stream):
    list_of_media = []
    counter = 1
    for available in stream:
        if available.resolution:
            temp = {
                    "id" : str(counter),
                    "resolution" : available.resolution,
                    "format" : available.mime_type
                }
        if not temp in list_of_media:
            list_of_media.append(temp)
        counter += 1
    return list_of_media