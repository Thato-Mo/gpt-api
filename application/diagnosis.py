import os
import sys
from keys import *
from pdf_input import *
import requests

def getFiles():

    path = './../rsrcs/'

    ext = '.pdf'

    all_types = os.listdir(path)

    prefix = '../rsrcs/'

    pdfs = [prefix + file for file in all_types if file.endswith(ext)]

    return pdfs

def diagnose(letter):
    api_url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {london_key}",
        "Content-Type": "application/json"
    }

    params = {
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": f"Give a sample diagnoses for the patient in the following referral letter: {pdf_to_text(letter)}. Return the patients name followed by the most likely diagnoses based on the patient's symptoms."}],
     "temperature": 0.7
    }

    response = requests.post(api_url, headers=headers, json=params)

    if response.status_code == 200:
        content =  response.json()['choices'][0]['message']['content']
        # result = {"doctor":content[2].split(':')[1],
        #           "patient":content[1].split(':')[1],
        #           "symptoms":content[0].split(':')[1]}
        return content
    else:
        return f"Error: {response.status_code} - {response.text}"
    
def batch_diagnose():
    letters = getFiles()

    # print(len(letters))

    for letter in letters:
        print(diagnose(letter))
    


if __name__ == "__main__":
    batch_diagnose()

