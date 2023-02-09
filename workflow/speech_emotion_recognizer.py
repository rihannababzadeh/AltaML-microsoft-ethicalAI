import os
import time

import azure.cognitiveservices.speech as speechsdk
import ktrain
from dotenv import load_dotenv


def speech_recognizer(file: str, _key_path: str) -> str:
    """performs continuous speech recognition with input from an audio file

    :param file: A string to the audio file
    :param _key_path: A string to the path to authenticate subscription for using Azure cognitive services
    """
    load_dotenv(_key_path)
    _subs_key = os.getenv("SUBSCRIPTION_KEY")
    _subs_region = os.getenv("REGION")
    speech_texts = []
    speech_config = speechsdk.SpeechConfig(subscription=_subs_key,
                                           region=_subs_region)
    audio_config = speechsdk.audio.AudioConfig(filename=file)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,
                                                   audio_config=audio_config)

    done = False

    def stop_cb(evt):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        nonlocal done
        done = True

    speech_recognizer.recognized.connect(
        lambda x: speech_texts.append(x.result.text))
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)
    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)
    speech_recognizer.stop_continuous_recognition()
    text_result = [' ' + sentence for sentence in speech_texts[1:]]
    text_result.insert(0, speech_texts[0])
    full_text_result = ''.join(text_result[:])
    return full_text_result


def emotion_mining_from_text(message: str, model_path: str) -> str:
    '''
    An extended version of BERT is used to evaluate emotions from
    text.

    :param message: A string that includes a message to be passed through the trained model
    :param model_path: A string path to the pre-trained tensorflow model
    '''
    predictor = ktrain.load_predictor(model_path)
    prediction = predictor.predict(message)
    return prediction
