
# Imports
from .Calls.openCalls import openCall
from .Calls.playCalls import playCall



def callApp(query:str ):
    '''
This module handles the further processing of the query


written by Anirudh Madhusudhan


'''

    try: 
        query = query.lower()

        # Open commands
        if "open" in  query:
            openCall(query)

        # play commands 
        elif "play" in query:
            playCall(query)


        # help command
        elif "help" in query:
            pass

        # volume control commands
        elif "volume" in query:
            pass


        # get info commands
        elif "search" in query or "what" in query:
            pass
        
        # save a note command
        elif "note" in query and "save" in query:
            pass

        # set timer and alarm command
        elif "timer" in query or "alarm" in query:
            pass


        # calulation commands
        elif "calculate" in query or "s" in query:
            pass

        # get jokes
        elif "tell me a joke" in query or "joke" in query:
            pass



        # easter eggs 
        

    except:

        return "Sorry, The request function is not yet available."
