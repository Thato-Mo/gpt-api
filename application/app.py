from flask import Flask, render_template
from api import *
app = Flask(__name__)


@app.route('/')
def index():
    pdf_path = sys.argv[1]
    text = pdf_to_text(pdf_path)
    extracted_info = gpt_request(text)

    data = {
        'doctor': extracted_info.get('doctor', ''),
        'patient': extracted_info.get('patient', ''),
        'symptoms': extracted_info.get('symptoms', ''),
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
     app.run(debug=True)
