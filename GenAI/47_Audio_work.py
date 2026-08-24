import os
from openai import OpenAI

client = OpenAI()

# Open up english translation audio
with (audio_file := open("hi.mp3", "rb")):
    transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
    
# Transcribe the phrase Hello my name is frank and i'm saying 

# stuff I hope that OpenAI can transcribe
print("Transcribing hi.mp3:\n")
print(transcript)

# Open up french translation audio
print("\nTranslating french.mp3:\n")

# Translate the phrase Je ne parle pas francais into english
with(audio_file := open("French.mp3", "rb")):
    transcript = client.audio.translations.create(model="whisper-1", file=audio_file)
    


#Will it actually work?
print(transcript)