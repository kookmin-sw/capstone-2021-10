from flask import Flask, render_template, redirect, request, url_for
from flask import send_from_directory
from flask import send_file
from pytube import YouTube
import spliter

app = Flask(__name__)

TITLE = ""
Thumb = ""
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
        fileName = spliter.split(yt.title)
        global Thumb
        Thumb= yt.thumbnail_url
    else:
        temp = None
    return redirect(url_for('down', title=fileName))

@app.route('/seperate_done/<title>')
def down(title=None):
    fileName = title
    global TITLE
    TITLE = fileName
    global Thumb
    return render_template('download.html', fileName=fileName, thumb=Thumb)


@app.route('/vocal_download')
def vocal_download():
    global TITLE
    fileName = TITLE
    file_name = f"seperated_audio/{fileName}/vocals.wav"
    return send_file(file_name,
                      mimetype='wav',
                      attachment_filename=f'{fileName}.wav',
                      as_attachment=True)

@app.route('/bass_download')
def bass_download():
    global TITLE
    fileName = TITLE
    file_name = f"seperated_audio/{fileName}/bass.wav"
    return send_file(file_name,
                      mimetype='wav',
                      attachment_filename=f'{fileName}.wav',
                      as_attachment=True)

@app.route('/drum_download')
def drum_download():
    global TITLE
    fileName = TITLE
    file_name = f"seperated_audio/{fileName}/drums.wav"
    return send_file(file_name,
                      mimetype='wav',
                      attachment_filename=f'{fileName}.wav',
                      as_attachment=True)
@app.route('/others_download')
def others_download():
    global TITLE
    fileName = TITLE
    file_name = f"seperated_audio/{fileName}/other.wav"
    return send_file(file_name,
                      mimetype='wav',
                      attachment_filename=f'{fileName}.wav',
                      as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
