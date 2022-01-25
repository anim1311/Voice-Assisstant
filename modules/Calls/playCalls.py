from re import T
import re
from .. import webbrowser
import os
from .spotifyAPI import spotifyAPI



def playCall(query:str):
    
    
    """
    This module handles all of the play calls

    Written by Anirudh Madhusudhan

    """


    if "youtube" in query:
        
        #https://www.youtube.com/results?search_query=german
        query = query.replace("youtube"," ")
        query = query.replace("play"," ")
        webbrowser.open("https://www.youtube.com/results?search_query="+query)
        return "Playing "+query+" on youTube"

 
    
    elif "spotify" in query:
        query = query.replace("spotify"," ")
        query = query.replace("on"," ")
        query = query.replace("play"," ")
        resp = spotifyAPI(query)
        try:
            os.system("cscript spotify.vbs "+ resp[1])
            return ("Playing "+query+" on Spotify App")
        except os.error:
            webbrowser.open(resp[0])
            return "Playing "+query+" on Spotify web"
        except:
            return "Spotify could not be opened"
    

