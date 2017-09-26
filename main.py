import os
import json
import SpotifyAPI
import Deluxer


crawler = SpotifyAPI.SpotifyAPI()
deluxer = Deluxer.Deluxer()
spotify_token = 'BQBWPyDIYgMIkBlGqdXm7LK9Lo15JB6AMbnZgTDvKR7dKjBdKF7Tg1hEh8clgpddhldrsR6uBPkkEX-B1nCCRrjVb4yJ0ghz-PHpke-BpkWchknxKX9toFEpQ7m7HOssWfxdgbfWvajQ_nlO'
path_artists = 'test'

# Read previously created dictionary into $data
json_data = open('data.txt').read()
data = json.loads(json_data)

artist_ids = {}
artists_not_found = []
albums_not_found = {}
deluxe_albums = {}

# Iterate through directory, first level is artist folders
for local_artist in os.listdir(path_artists):
    # Use artist name to find artist_id
    artist_id = crawler.GetArtistIDFromSearch(local_artist, spotify_token)
    # If artist doesn't exist on Spotify, add to list and continue at next artist
    if artist_id == 0:
        artists_not_found.append(local_artist)
        continue

    # Artist exists and we have their $artist_id

    # Get all of artist's albums on Spotify
    sp_albums_data = crawler.GetAlbumsFromArtistID(artist_id, spotify_token)
    # If the artist has no albums, continue at next artist
    if len(sp_albums_data) < 1:
        continue
    # Create list of all of artists album names
    sp_album_names = []
    for sp_album in sp_albums_data['items']:
        sp_album_names.append(sp_album['name'])

    # Iterate through directory, second level is album folders
    path_albums = path_artists + "\\" + local_artist
    for local_album in os.listdir(path_albums):
        # Check if local album is in Spotify albums list
        if any(local_album in s for s in sp_album_names):
            # Local album is on Spotify...
            # Iterate through directory, third level is either song files or disc folders
            path_songs = path_albums + "\\" + local_album
            #for local_song in os.listdir(path_songs):
            #    if os.path.isdir(local_song):
            #        # Disc Folder
            #    else:
            #        # Check if song is liked on Spotify

            #https: // api.spotify.com / v1 / me / tracks / contains

        else:
            albums_not_found[local_artist] = local_album
    # Now have a list of all local albums not found on Spotify

with open('artists.txt', 'w') as outfile:
    json.dump(artists_not_found, outfile, indent=4)

with open('albums.txt', 'w') as outfile:
    json.dump(albums_not_found, outfile, indent=4)

print(deluxe_albums)
