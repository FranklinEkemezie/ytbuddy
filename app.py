from flask import Flask, request, render_template, redirect, url_for
import yt_dlp
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the YouTube Downloader!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
