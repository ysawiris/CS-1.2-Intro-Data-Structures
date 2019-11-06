from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from modules import sample_by_frequency, frequency
import os 

app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Lryic-Generator')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
lyric = db['lyric']


@app.route('/')
def index():
    """Return homepage"""
    lyric_list = {
        'lyric' : sample_by_frequency.run_sample_by_freq()
    }
    lyric_id = lyric.insert_one(lyric_list).inserted_id
    return render_template('base.html', lyric_id = lyric_id)



if __name__ == '__main__':
    app.run(debug=True)