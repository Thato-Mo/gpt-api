from flask import Flask, render_template
import sys
import requests
import json
from keys import *
from pdf_input import *

def gpt_request(text):
    api_url = "https://api.openai.com/v1/chat/completions"
    
headers = {
        "Authorization": f"Bearer {london_key}",
        "Content-Type": "application/json"
    }

params = {
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": f"Isolate the symptoms, patient's name, and doctor's name from the following text: {text} return the catgories a three seperate strings"}],
     "temperature": 0.7
    }

    response = requests.post(api_url, headers=headers, json=params)
    
    if response.status_code == 200:
        content =  response.json()['choices'][0]['message']['content'].split('\n')
        result = {"doctor":content[2].split(':')[1],
                  "patient":content[1].split(':')[1],
                  "symptoms":content[0].split(':')[1]}
        return result
    else:
        return f"Error: {response.status_code} - {response.text}"
    

@app.route('/')
def index():
    pdf_path = sys.argv[1]
    text = pdf_to_text(pdf_path)
    gpt = gpt_request(text)
    
    data = { "doctor", "patient",  "symptoms"            
    }
        
    return render_template('index.html', data=data)

if __name__ == '__main__':
    # index(sys.argv[1])
    app.run(debug=True)
    

    