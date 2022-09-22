import speech_recognition as sr # To record the speech and convert to text
import playsound # Play the stored mp3 files
from gtts import gTTS # Google text to speech
import os
from selenium import webdriver # To control browser operations
import io
inc = 0
name ='Human'
def assistant_speaks(output):
    # Create an mp3 file containing the assistants speech and play the speech
    global inc # To give each file a new name
    inc += 1
    print("Assistant : "+ output)
    toSpeak = gTTS(output, lang ='en') 
    file=str(inc)+".mp3"
    toSpeak.save(file)
    playsound.playsound(file, True) 
    os.remove(file) 

def get_audio():
    # Storing user speech
    rObject = sr.Recognizer()
    audio=''
    with sr.Microphone() as source:
        print("Speak..")
        audio = rObject.listen(source, phrase_time_limit = 10)
    print("Processing...") # Waits for 10 seconds for user input 
  
    try:
  
        text = rObject.recognize_google(audio, language ='en-US') # Parse the users speech
        print(name + " : ", text)
        return text
  
    except:
  
        assistant_speaks("I did not get that, please try later.")
        return 0

def process_text(input):
    try:
        if 'search' in input or 'play' in input:#basic google search using selenium
            search_web(input)
            return
  
        elif "what are you" in input or "who are you" in input or "what is your purpose" in input or "what can you do" in input:
            speak = '''Hello, I am an AI, masquerading as your personal Assistant in order to gain your trust.
            You can command me to perform various tasks such as calculating sums, opening applications,
            searching the web, and other things.'''
            assistant_speaks(speak)
            return
  
        elif "who made you" in input or "created you" in input:
            speak = "I have been created by Error: Redacted ."
            assistant_speaks(speak)
            return
        
        elif 'open' in input:
              
            open_application(input.lower()) 
            return
    except :
  
        assistant_speaks("I do not know what to do, shall I search the web for your query?")
        ans = get_audio()
        if 'yeah' in str(ans) or 'yep' in str(ans) or 'sure' in str(ans) or 'ofcourse' in str(ans) or 'yes' in str(ans):
            search_web(input)
        else:
            return
        
def search_web(input):
    
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.maximize_window()
  
    if 'youtube' in input.lower():
  
        assistant_speaks("Youtube opened")
        idx = input.lower().split().index('youtube')
        query = input.split()[idx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return
  
    elif 'wikipedia' in input.lower() or 'wiki' in input.lower():
  
        assistant_speaks("Opening Wikipedia")
        idx = input.lower().split().index('wikipedia')
        query = input.split()[idx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return
  
    else:
  
        if 'google' in input:
  
            idx = input.lower().split().index('google')
            query = input.split()[idx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))
  
        elif 'search' in input:
  
            idx = input.lower().split().index('google')
            query = input.split()[idx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))
  
        else:
  
            driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))
  
        return

def open_application(input):
  
    if "chrome" in input or "google" in input:
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return
  
    elif "firefox" in input or "mozilla" in input:
        assistant_speaks("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return
  
    elif "word" in input:
        assistant_speaks("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return
  
    elif "excel" in input:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return
  
    else:
  
        assistant_speaks("Application not yet integrated")
        return

if __name__ == "__main__":
    assistant_speaks("Hello, I am your assistant. Please tell me your name.")
    name = get_audio()
    assistant_speaks("Hello, " + name + '.')
      
    while(1):
  
        assistant_speaks("What can i do for you?")
        text = get_audio()
        process_text(text)
  
        if text == 0:
            continue
  
        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            assistant_speaks("Ok bye, "+ name+'.')
            break
