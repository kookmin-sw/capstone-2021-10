from flask import Flask, render_template, redirect, request, url_for
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
@app.route('/<link>')
def inputTest(link=None):
    return render_template('main.html', link=link)

@app.route('/getLink', methods=['POST'])
def getLink(link=None):
    if request.method == 'POST':
        temp = 'succ'
        yt = YouTube(request.form['link'])
        yt.streams.filter(only_audio=True).first().download()
    else:
        temp = None
    return redirect(url_for('inputTest', link=temp))

if __name__ == '__main__':
    app.run()
