#!/usr/bin/venv python3
"""
app.py -
"""

import os
from utils import dir_files
from flask import Flask, render_template, send_from_directory


def _create_app():
    """Creates the flask web server instance
    """
    app = Flask(__name__, static_folder='static', static_url_path='')
    return app

app = _create_app()


# @app.route('/images/<path:filename>')
# def static_images(filename):
#     """Send images
#     """
#     return send_from_directory('../images/', filename)


@app.route("/")
def root():
    """Root for website
    """
    images = []
    i = 1
    for root, dirs, files in os.walk('./veggie-on-rails/static/images'):
        for file in files:
            images.append((i, file))

    # for i in range(len(files)):
    #    images.append((i, files[i]))
    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
