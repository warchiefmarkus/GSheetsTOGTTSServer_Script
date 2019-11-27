# -*- coding: utf-8 -*-   
from google.cloud import texttospeech
import os, sys

def generate_mp3(cell, name):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/var/www/html/gapp/ttsgoogle-3564fd70a2bb.json"
    client = texttospeech.TextToSpeechClient()
    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(ssml=cell)

    #ssml="<speak>To be</speak>"
    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(language_code='en-US',ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    #The response's audio_content is binary.
    #with io.open("/var/www/html/gapp/sounds/"+name, 'wb') as out:
         # Write the response to the output file.
         #out.write(response.audio_content)
    sys.stdout.write(response.audio_content)
    #return "SOME RETURN"


if __name__ == '__main__':
    a = sys.argv[1]
    b = sys.argv[2]
    generate_mp3(a,b)