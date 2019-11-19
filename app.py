from flask import Flask, request, render_template, jsonify, send_from_directory, redirect
import os
import json

from modules.draw import draw




app = Flask(__name__)
PEOPLE_FOLDER = os.path.join('result', '')




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/LICENSE')
def license():
    return render_template('LICENSE.html')

@app.route('/result/<path:filename>')
def image(filename):
    return send_from_directory("result", filename, as_attachment=('download' in request.args))



@app.route('/show/<path:filename>')
def show(filename):
    file = os.path.join('result', filename + ".png")
    if os.path.exists(file):
        return render_template("show.html", image=filename)
    else:
        return render_template('404.html'), 404

@app.route('/make_by_text', methods=['POST'])
def make_by_text():
    file = request.files

    data_dist = request.values.to_dict()
    try:
        file_file = file['file']
    except:
        return '/404'
    f_n = data_dist['f_n']
    l_n = data_dist['l_n']
    pat = data_dist['pat']
    gend = data_dist['gend']
    if (f_n == '') or (l_n == '') or (pat == '') or (gend == ''):
        return '/404'

    face = 'faces/' + file_file.filename

    #print(str(file_file))
    #print(file_file.filename)
    file_file.save('faces/' + file_file.filename)
    #print(f_n)
    #print(l_n)
    #print(pat)
    #print(gend)
    semple_input = '1'
    if (gend == "Man") or (gend == 'MAN'):
        gend = 'M'
    elif (gend == "Woman") or (gend == 'WOMAN'):
        gend = 'F'
    else:
        return render_template('404.html'), 404
    #print(name)
    name = draw(semple_input, f_n, l_n, pat, gend, face)
    if name == 'error':
        return '/404'
    else:
        return '/show/' + name

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)