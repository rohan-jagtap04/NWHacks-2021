# pip install spacy
# python -m spacy download en_core_web_sm
from google.cloud import speech
import os
import io
import spacy

class Speech_Processing(object):

    def __init__(self, audio):
        self.client = speech.SpeechClient()
        self.audio = audio
        self.config = speech.RecognitionConfig(
          encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
          audio_channel_count=2,
          language_code="en-US",
        )

    def SpeechToText(self):
      response = self.client.recognize(request={"config": self.config, "audio": self.audio})
      audioTranscript = ""
      for result in response.results:
        audioTranscript += result.alternatives[0].transcript
      return audioTranscript

    