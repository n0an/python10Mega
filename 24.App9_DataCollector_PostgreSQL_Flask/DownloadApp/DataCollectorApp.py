from flask import Flask, render_template, request, send_file

from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download')
def download():
    return send_file(new_filename,
                     attachment_filename='yourfile.txt',
                     as_attachment=True)


@app.route('/success', methods=['POST'])
def success():
    global new_filename
    if request.method == 'POST':


        file_uploaded = request.files["file"]

        new_filename = 'uploaded'+file_uploaded.filename

        file_uploaded.save(secure_filename(new_filename))

        print(file_uploaded)
        print(type(file_uploaded))

        with open(new_filename, 'a') as fin:
            fin.write('added line')

        return render_template('index.html', btn='download.html')




if __name__ == '__main__':
    app.run(debug=True)
