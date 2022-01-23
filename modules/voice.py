'''
This module handles the speech recognition and text to voice function


written by Anirudh Madhusudhan


'''





try:
    import speech_recognition as sr
    import pyttsx3
except ImportError:
    raise ImportError('There are some missing imports. please run the commadn pip install -r requirements.txt')

# Initialize the recognizer 
r = sr.Recognizer() 
def SpeakText(command):
    print(command)
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
       
      
def getSpeech():
    try:
        with sr.Microphone() as source2:
              
            r.adjust_for_ambient_noise(source2, duration=0.2)

            print("Listening...") 
            #listens for the user's input 
            audio2 = r.listen(source2)
              
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()     
            return MyText
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("Didn't get it you")
    except:
        print("Didn't get it")