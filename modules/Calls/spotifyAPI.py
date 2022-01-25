# To access Spotipy
import spotipy
# To View the API response
import json
import os
#Getting the Api codes from a file
from ...settings import *

username =spotifyUsername
clientID = spotifyClientID
clientSecret =spotifyClientSecret
redirectURI = 'http://google.com/' 

def spotifyAPI(searchQuery):
    # Create OAuth Object
    oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
    # Create token
    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']
    # Create Spotify Object
    spotifyObject = spotipy.Spotify(auth=token)

    user = spotifyObject.current_user()
    # To print the response in readable format.
    #print(json.dumps(user,sort_keys=True, indent=4))

    
    searchResults = spotifyObject.search(searchQuery,1,0,"track")

    tracks_dict = searchResults['tracks']
    tracks_items = tracks_dict['items']
    song = tracks_items[0]['external_urls']['spotify']
    uri = tracks_items[0]["uri"]
    return song,uri
