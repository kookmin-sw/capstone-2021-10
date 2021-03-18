import spliter, os
from flask import Flask, render_template, redirect, request, url_for
from flask import send_from_directory
from flask import send_file
from werkzeug import secure_filename
from pytube import YouTube


app = Flask(__name__)

TITLE = ""
THUMB = ""
STEMS = 0
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
        global THUMB
        THUMB= yt.thumbnail_url
        global STEAMS
        STEAMS = request.form.get('steams')
        fileName = spliter.split(yt.title,STEAMS)
    else:
        temp = None
    return redirect(url_for('down', title=fileName))

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/fileupload', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
<<<<<<< HEAD
        f.save("./uploads/" + secure_filename(f.filename))
        fileName=spliter.split(f.filename[:-4])
        global STEAMS
        STEAMS = request.form.get('steams')
        return redirect(url_for('down', title=fileName))
=======
        f.save(secure_filename(f.filename))
        fileName=spliter.split(f.filename[:-4])
        return redirect(url_for('down', title=fileName)) 
>>>>>>> d1b50a754a811c99a039d3fe155af47136db0559

@app.route('/seperate_done/<title>')
def down(title=None):
    fileName = title
    global TITLE
    TITLE = fileName
    global STEAMS, THUMB
    return render_template('download.html', fileName=fileName, steams=STEAMS, thumb= THUMB)


@app.route('/vocal_download')
def vocal_download():
    global TITLE
    fileName = TITLE
    file_name = f"seperated_audio/{fileName}/vocals.wav"
    return send_file(file_name,
                      mimetype='wav',
                      attachment_filename=f'{fileName}_vocal.wav',
                      as_attachment=True)

@app.route('/bass_download')
def bass_download():
    global TITLE
    fileName = TITLE
    file_name = f"seperated_audio/{fileName}/bass.wav"
    return send_file(file_name,
                      mimetype='wav',
                      attachment_filename=f'{fileName}_bass.wav',
                      as_attachment=True)

@app.route('/drum_download')
def drum_download():
    global TITLE
    fileName = TITLE
    file_name = f"seperated_audio/{fileName}/drums.wav"
    return send_file(file_name,
                      mimetype='wav',
                      attachment_filename=f'{fileName}_drum.wav',
                      as_attachment=True)
@app.route('/others_download')
def others_download():
    global TITLE
    fileName = TITLE
    file_name = f"seperated_audio/{fileName}/other.wav"
    return send_file(file_name,
                      mimetype='wav',
                      attachment_filename=f'{fileName}_others.wav',
                      as_attachment=True)

@app.route('/piano_download')
def piano_download():
    global TITLE
    fileName = TITLE
    file_name = f"seperated_audio/{fileName}/piano.wav"
    return send_file(file_name,
                      mimetype='wav',
                      attachment_filename=f'{fileName}_piano.wav',
                      as_attachment=True)



if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
