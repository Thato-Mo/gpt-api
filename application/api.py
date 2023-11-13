import requests
import sys
from keys import *
from pdf_input import *


def gpt_request(text):
    '''Reads text and returns information needed
    Args:
        text: takes string data to be read by gpt
    '''

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
        content = response.json()['choices'][0]['message']['content'].split('\n')
        if len(content) >= 3:
            doctor = content[2].split(':')[1].strip()
            patient = content[1].split(':')[1].strip()
            symptoms = content[0].split(':')[1].strip()
            return {"doctor": doctor, "patient": patient, "symptoms": symptoms}
        else:
            return {"error": "Incomplete response from the API"}
    else:
        return {"error": f"Error: {response.status_code} - {response.text}"}

if __name__ == "__main__":
    print(gpt_request(pdf_to_text(sys.argv[1])))
