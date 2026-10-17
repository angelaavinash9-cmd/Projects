import os
import speech_recognition as sr 
from googletrans import Translator
from gtts import gTTS
import pygame 

def speak(text, language="hi"):
    if not text.strip():
        return

        filename = "temp_translation.mp3"

        try:
            tts=gTTs(text=text, lang=language, slow=false)
            tts.save(filename)

            pygame.mixer.init()
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            pygame.mixer.quit()
            if os.path.exists(filename):
                os.remove(filename)
        except Exception as e:
            print(f" Errorplaying audio: {e}")
            
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("/n Adjusting for background noise...Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=0.8)
        print("Please speak now in English....")
        audio = recognizer.listen(source)
    try:
        print("Recognising speech...")
        text = recognizer.recognize_google(audio, language="en-Us")
        print(f"You said:{text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f" API Error: {e}")
    return ""

def translate_text(text, target_language="hi"):
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        print(f"Translated text({target_language}): {translation.text}")
        return translation.text

def display_language_options():
        print("/n Select Target Translation Language:")
        print("1. Hindi (hi)")
        print("2. Tamil (ta)")
        print("3. Telugu (te)")
        print("4. Bengali (bn)")
        print("5. Marathi (mr)")
        print("6. Gujararti (gu)")
        print("7. Malayalam (ml)")
        print("8. Punjabi (pa)")

        choice = input("PLease slect choice (1-8): ").strip()
        language_dict = {
            "1": "hi",
            "2": "ta",
            "3": "te",
            "4": "bn",
            "5": "mr",
            "6": "gu",
            "7": "ml",
            "8": "pa",
        }

        return language_dict.get(choice,"hi")

def main():
        target_language = display_language_options()

        original_text = speech_to_text()

        if original_text:

            translated_text = translate_text(
                original_text, target_language=target_language
            )

            print("Speaking translation....")
            speak(translated_text, language=target_language)
            print("Finished speaking!")

if __name__ == "__main__":
    main()    
        

     


