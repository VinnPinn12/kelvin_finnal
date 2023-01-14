from flask import Flask, render_template, request, jsonify, redirect, url_for
import certifi
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(cxn_str, tlsCAFile=certifi.where())
db = client.dbsparta_plus_week3


@app.route("/")
def main():
    return render_template("prac_map.html")



if __name__ == "__main__":
    app.run("0.0.0.0", port=5001, debug=True)