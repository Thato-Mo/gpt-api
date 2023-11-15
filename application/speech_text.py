import os
from keys import london_key
from openai import OpenAI

api_key = london_key # Replace with your actual API key
os.environ["OPENAI_API_KEY"] = api_key

client = OpenAI(api_key=api_key)


audio_file= open("../rsrcs/audio_text.m4a", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print (transcript)

