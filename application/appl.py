from flask import Flask, render_template
import sys

app = Flask(__name__)

def open_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

@app.route('/')
def index():

    text = open_text_file(sys.argv[1])

    data = {
        'text': text,
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    # index(sys.argv[1])
    app.run(debug=True)