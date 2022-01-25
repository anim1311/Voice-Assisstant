

import warnings
import os
warnings.simplefilter("ignore")
from distutils.log import error
from .. import webbrowser



def openCall(query):

    """
This module handles all of the open calls

Written by Anirudh Madhusudhan

"""
    # open browser
    try:
        if "youtube" in query:
            webbrowser.open("www.youtube.com")
        
        elif "spotify" in query:
            try:
                os.system("Spotify.exe")
            except os.error:
                webbrowser.open("https://open.spotify.com/")
            except:
                return "Spotify could not opened"
                

        elif "chrome" in query:
            try:
                webbrowser.Chrome.open("www.google.com")
            except:
                return("Chrome has not been installed")
        elif "morizlla" in query:
            try:
                webbrowser.Mozilla.open("www.google.com")
            except:
                return("Mozilla has not been installed")
        elif "opera" in query:
            try:
                webbrowser.Opera.open("www.google.com")
            except:
                return("Opera has not been installed")
        
        



    except error as e:
        return "The functionality has not yet been added"
    
