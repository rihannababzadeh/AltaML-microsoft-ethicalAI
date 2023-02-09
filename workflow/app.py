import os
import warnings
from pathlib import Path

from speech_emotion_recognizer import (emotion_mining_from_text,
                                       speech_recognizer)
from utils import load_yaml_config, parse_arguments

warnings.simplefilter("ignore", UserWarning)
arguments = parse_arguments(arguments_list=None)
config = load_yaml_config(config_path=Path(
    __file__).parent / arguments.config_path)
data_path = config['data_path']


def extract_emotion(filepath: str = None):
    '''
    Emotion mining is done on all .wav files within the data_path.
    '''
    if filepath is None:
        for file in os.listdir(data_path):
            if file.endswith('.wav'):
                text_from_speech = speech_recognizer(
                    os.path.join(data_path, file), config['key_path'])
                print(f'Speech to text:\n {text_from_speech}')
                predicted_emotion = emotion_mining_from_text(
                    text_from_speech, config['bert_model_path'])
                print(
                    f'\nPrediction result for {file}: --{predicted_emotion}--')

    else:
        text_from_speech = speech_recognizer(filepath, config['key_env_path'])
        print(f'Speech to text:\n {text_from_speech}')
        predicted_emotion = emotion_mining_from_text(text_from_speech,
                                                     config['bert_model_path'])
        print(f'\nPrediction result for {file}: --{predicted_emotion}--')


if __name__ == '__main__':
    extract_emotion()
