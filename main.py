import os
import json
import SpotifyAPI
import Deluxer


crawler = SpotifyAPI.SpotifyAPI()
deluxer = Deluxer.Deluxer()
spotify_token = 'BQC_rPsMv8hAaoNYLu4Bn2s-iza41Ffi4QqTW_7zwVWlHOskYnXjr75JhwwTwxyWukc5eIrEK3f9SdLr0-LBVCeYl6EHAf0nocHFhLbwXHsVep3b48CBg8obuEmKzC0SajVTBwQgAVt57VkO'
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
    albums_data = crawler.GetAlbumsFromArtistID(artist_id, spotify_token)
    # If the artist has no albums, continue at next artist
    if len(albums_data) < 1:
        continue
    # Create list of all of artists album names
    album_names = []
    for album in albums_data['items']:
        album_names.append(album['name'])

    # Iterate through directory, second level is album folders
    path_albums = path_artists + "\\" + local_artist
    for local_album in os.listdir(path_albums):
        # Check if local album is in Spotify albums list
        if not any(local_album in s for s in album_names):
            # If not, check if album name has deluxe
            if "Deluxe" in local_album:
                deluxe_album = deluxer.FixDeluxeAlbum(local_album, spotify_token)
                # If deluxe album was found, rename directory
                if deluxe_album != local_album:
                    os.rename(path_albums + "\\" + local_album, path_albums + "\\" + deluxe_album)
            # If album was not deluxe or didn't find a correct name, add to $albums_not_found list
            albums_not_found[local_artist] = local_album
    # Now have a list of all local albums not found on Spotify

with open('artists.txt', 'w') as outfile:
    json.dump(artists_not_found, outfile, indent=4)

with open('albums.txt', 'w') as outfile:
    json.dump(albums_not_found, outfile, indent=4)

print(deluxe_albums)
