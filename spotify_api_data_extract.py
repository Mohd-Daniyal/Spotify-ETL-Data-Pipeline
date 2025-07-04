import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
import boto3

def lambda_handler(event, context):
    
    cilent_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    
    client_credentials_manager = SpotifyClientCredentials(client_id=cilent_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlists = sp.user_playlists('spotify')
    
    playlist_link = "https://open.spotify.com/playlist/4nqbYFYZOCospBb4miwHWy"
    playlist_URI = playlist_link.split('/')[-1]
    
    spotify_data = sp.playlist_tracks(playlist_URI)

    client = boto3.client('s3')
    
    filename = "spotify_raw_" + str(datetime.now()) + ".json"

    client.put_object(
        Bucket="spotify-etl-project-mdh",
        Key="raw_data/to_processed/" + filename,
        Body=json.dumps(spotify_data)
        )

    print(spotify_data)
