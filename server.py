# From root
# export FLASK_APP=server/server.py
# export FLASK_ENV=development
# Because tensorflow, by default, preallocates memory (I don't know how much) and this causes it to quickly run out of
# memory, particularly if you are running many jobs at once. This allows the memory to grow
# export TF_FORCE_GPU_ALLOW_GROWTH='true'
# flask run
# test endpoint by:
# curl -F "file=@ocr/sudoku8.jpg" -X POST -o solution.jpg localhost:5000/sudoku
import io

import cv2
import numpy
from flask import Flask, request, send_file

import main

app = Flask(__name__)


@app.post('/sudoku')
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        # uploaded_file.save(uploaded_file.filename)
        cv2_image = cv2.imdecode(numpy.fromstring(uploaded_file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
        solved_cv2 = main.solve(cv2_image)
        res, solved_jpg = cv2.imencode(".jpg", solved_cv2)

        return send_file(
            io.BytesIO(solved_jpg),
            mimetype='image/jpg',
            as_attachment=True,
            attachment_filename='solved.jpg')
    return "Internal error, sorry, x(", 500
