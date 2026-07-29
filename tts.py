import speech_recognition as sr
import pyttsx3
import sounddevice as sd
import numpy as np
from deep_translator import GoogleTranslator

def speak(text, language= "en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    sample_rate = 16000
    duration = 5

    print("please speak now in english, 5 secs max")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()

    try:
        print("recognizing speech...")
        audio_bytes=audio_data.tobytes()
        audio=sr.AudioData(audio_bytes, sample_rate, 2)

        text = recognizer.recognize_google(audio, language="en-UK")
        print(f" you said: {text}")
        return text
    except sr.UnknownValueError:
        print("could not understand the audio.")
    except sr.RequestError as e:
        print(f" API Error: {e}")
        return ""

def translate_text(text, target_language="es"):
    translator = GoogleTranslator(source='auto', target = target_language)
    translation = translator.translate(text)
    print(f"translated text: {translation}")
    return translation

def display_language_options():
    print ("available language translations: ")
    print (" 1. urdu (ur)")
    print ("2. spanish (es)")
    print ("3. german (de)")
    print ("4. japanese (ja)")
    print ("5. korean (ko)")
    print ("6. mandarin (zh-CN)")
    print ("7. russian (ru)")
    print ("8. italian (it)")

    choice = input("please select the target language number (1-8): ")
    language_dict= {
        "1": "ur",
        "2": "es",
        "3": "de",
        "4": "ja",
        "5": "ko",
        "6": "zh-CN",
        "7": "ru",
        "8": "it"
    }
    return language_dict.get(choice, "es")

def main():
    target_language = display_language_options()
    original_text = speech_to_text()

    if original_text:
        translated_text = translate_text(original_text, target_language = target_language)
        speak(translated_text)
        print("translation spoken out.")

if __name__ == "__main__":
    main()