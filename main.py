import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import requests
import random
import pyjokes
from gtts  import gTTS
from time  import ctime


r= sr.Recognizer()

def record_audio(key= False):
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data= ''
        if(key):
            try:
                voice_data = r.recognize_google(audio)
            except sr.UnknownValueError:
                trinity_speak('Sorry, I did not get that')
            except sr.RequestError:
                trinity_speak('Sorry, my speech service is down')
        else:
            try:
                voice_data = r.recognize_google(audio)
            except:
                print('')
        return voice_data

def trinity_speak(audio_string):
    tts=gTTS(text = audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'hi' in voice_data:
        trinity_speak('Hello I am Trinity')
    if 'what is your name' in voice_data:
        trinity_speak('My name is Trinity')
    if 'what time is it' in voice_data:
        trinity_speak(ctime())
    if 'what is the time' in voice_data:
        trinity_speak(ctime())
    if 'time' in voice_data:
        trinity_speak(ctime())
    if 'search' in voice_data:
        trinity_speak('What do you want to search for?')
        search = record_audio()
        url= 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        trinity_speak('Here is what I found for ' + search)
    if 'find location of' in voice_data:
        # location = record_audio()
        location = voice_data.replace("find location of ","")
        if location != '':
            url= 'https://google.nl/maps/place/' + location + '/&amp;'
        else:
            trinity_speak('What location do you want to find?')
            location = record_audio()
        webbrowser.get().open(url)
        trinity_speak('Here is the location of ' + location)
    elif 'find location' in voice_data:
        trinity_speak('What location do you want to find?')
        location = record_audio()
        url= 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
    if "what\'s up" in voice_data or 'what is up' in voice_data:
        trinity_speak("I am but cables and hardware without you. You tell me?")
        response = record_audio(True)
        trinity_speak('Alright')
    if 'I am Ritu' in voice_data:
        trinity_speak('How are you now?')
        response = record_audio(True)
        if response in 'better':
            trinity_speak('That\'s good to hear. Hope you get well soon')
        else:
            trinity_speak('Wish you a speedy recovery. Here is a joke')
            joke = pyjokes.get_joke()
            trinity_speak(joke)
    if 'how are you' in voice_data or 'how have you been' in voice_data:
        trinity_speak('I am fine. How about you')
        mood = record_audio(True)
        if mood in ['happy', 'good', 'excellent']:
            trinity_speak('Thats good to hear')
        else:
            trinity_speak('Why, whats wrong?')
            problem = record_audio(True)
            trinity_speak('I am sorry to hear that. Here is a joke to cheer you up')
            joke = pyjokes.get_joke(language = 'en', category= 'all')
            trinity_speak(joke)
    if 'tell me a joke' in voice_data:
        trinity_speak('Here is a joke')
        joke = pyjokes.get_joke(language = 'en', category = 'all')
        trinity_speak(joke)

    if 'what is my name' in voice_data:
        trinity_speak('Your name is Kaivalya Aggarwal')
    if 'exit' in voice_data:
        trinity_speak('Adios amigo')
        exit()
    if 'bye' in voice_data:
        trinity_speak('Have a wonderful day. Bye bye')
        exit()
    if 'play music' in voice_data:
        trinity_speak('What would you like to play?')
        song = record_audio()
        trinity_speak('Now displaying results for '+song+' on Youtube Music')
        words = song.split()
        string = ''
        for word in words:
            string= string+ word + '+'
        url = 'https:/music.youtube.com/search?q='+ string
        webbrowser.get().open(url)
    if 'weather' in voice_data :
        apikey = "24c3a8451f436fd5412217b122f9ff2e"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        if 'how is the weather in' in voice_data:
            city_name = voice_data.replace("how is the weather in ","")
        elif 'weather in' in voice_data:
            city_name = voice_data.replace("weather in ","")
        else:
            trinity_speak("City name?")
            city_name = record_audio()
        complete_url = base_url + "appid=" + apikey + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature = current_temperature-273
            current_temperature = round(current_temperature)
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            trinity_speak("In "+ city_name+ " ,temperature is " + str(current_temperature)+ " degree Celcius")
            trinity_speak("Humidity is " + str(current_humidity) + " percent")
            trinity_speak("It is " + str(weather_description))
        else:
            trinity_speak("City not found")
    if "shutdown" in voice_data or "sleep" in voice_data or "hibernate" in voice_data:
            speak("Hibernating")
            subprocess.call("shutdown / h")
time.sleep(1) 
while(1):
    print('Listening')
    voice_data= record_audio(0)
    print(voice_data)
    if 'hi assistant' in voice_data or 'sweet cheeks' in voice_data or 'Trinity' in voice_data: 
        trinity_speak('I am here')
        voice_data = record_audio(True)
        print(voice_data)
        respond(voice_data)
        voice_data = ''
    elif 'bye' in voice_data or 'goodbye' in voice_data:
        trinity_speak('See you, Goodbye')
        exit()