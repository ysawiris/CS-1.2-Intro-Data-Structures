from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from modules import markov_2nd_order, frequency
import os 

app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/create-lryic-gen')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
lyric = db['lyric']


@app.route('/')
def index():
    """Return homepage"""
    lyric_list = {
        'lyric' : markov_2nd_order.run_generator()
    }
    lyric_id = lyric.insert_one(lyric_list).inserted_id
    lyric_text = lyric.find_one({'_id': ObjectId(lyric_id)})['lyric']  
    return render_template('base.html', lyric_id = lyric_id, lyric_text = lyric_text)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))