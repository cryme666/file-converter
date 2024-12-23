from flask import Flask, request, redirect, url_for, render_template_string, render_template, flash, send_file
import os
from convert import *

app = Flask('Converter')

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = '123456789'

ALLOWED_EXTENSIONS = {'pdf', 'xlsx', 'jpg', 'png', 'txt','csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():

    file = request.files['file']
    convertion_type = request.form['conversion']

    if file.filename.rsplit('.')[1] in ALLOWED_EXTENSIONS:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
        file.save(file_path)
    else:
        # flash('Файл не підтримується нашою системою','error')
        return 'Файл не підтримується нашою системою', 400
    

    # може виникнути помилка тоді коли ми передамо excel але виберемо опцію jpg_to_png
    if convertion_type == 'jpg_to_png':
        converted_filename = jpg_to_png(f'{app.config["UPLOAD_FOLDER"]}/{file.filename}')
    elif convertion_type == 'png_to_jpg':
        converted_filename = png_to_jpg(f'{app.config["UPLOAD_FOLDER"]}/{file.filename}')
    elif convertion_type == 'excel_to_csv':
        converted_filename = excel_to_csv(f'{app.config["UPLOAD_FOLDER"]}/{file.filename}')
    elif convertion_type == 'csv_to_excel':
        converted_filename = csv_to_excel(f'{app.config["UPLOAD_FOLDER"]}/{file.filename}')
    elif convertion_type == 'txt_to_pdf':
        converted_filename = txt_to_pdf(f'{app.config["UPLOAD_FOLDER"]}/{file.filename}')


    return send_file(converted_filename,as_attachment=True), 200

    

if __name__ == '__main__':
    app.run(debug=True)