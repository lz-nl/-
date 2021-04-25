from flask import Flask, render_template
from pymongo import MongoClient

mydb = MongoClient('mongodb://localhost:27017').rb

app = Flask(__name__)

@app.route('/')
def index():
    mytable = mydb.rb
    result = mytable.find_one({"name": "lz"})
    print(result)
    return render_template('index.html', name=result["name"])

if __name__ == '__main__':
    app.run(debug=True)