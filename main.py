# IMPORTS ______________________
# custom imports
import modules.voice as voice
import modules.callApps as calls
# imports from default python library
import os















# Main Function

if __name__ == "__main__":

    os.system("title.bat")
    query= voice.getSpeech()
    print(query)
    calls.callApp(query)
