from flask import Flask, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
import csv
import numpy
import os

UPLOAD_FOLDER = os.path.abspath("./uploads")
ALLOWED_EXTENSIONS = {'csv'}
#f = 

app = Flask(__name__)
app.config["UPLOAD_FOLDER"]= UPLOAD_FOLDER
CORS(app)

[]

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/uploader", methods=["GET", "POST"])
def uploads():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part'
            
        file = request.files['file']

        if file.filename == '':
            return 'No selected file'
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'file uploaded successfully'
        else:
            return 'No allowed extension'

@app.route("/uploads/<filename>")
def get_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

#raw_data = open(f, 'r')
#reader = csv.reader(raw_data , delimiter=',', quoting=csv.QUOTE_NONE)
#x = list(reader) 
#data = numpy.array(x).astype('float')
#print(data.shape)

if __name__ == "__main__":
    app.run(debug=True)