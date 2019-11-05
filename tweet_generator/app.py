from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from modules import sample_by_frequency, frequency
import os 

app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Lryic-Generator')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()


@app.route('/')
def index():
    """Return homepage"""
    lyric = sample_by_frequency.run_sample_by_freq()
    return render_template('base.html')



if __name__ == '__main__':
    app.run(debug=True)