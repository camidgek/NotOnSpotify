import json
import SpotifyAPI
import PathFinder


crawler = SpotifyAPI.SpotifyAPI()
spotify_token = 'BQBs_b795Fx1tjNtre3DVtORopPFfEiTx2AM-wve1XUbf_KYkkVAoGn0r3C7Xv_-IyPU_KwqZzZN74YvyPF-QUI4ORsd6v9dynUqcH4yIhUfTWNE8_TIy5oAR8kVmMSk7m4ynRW2jWpIxEBF'
path = 'test'

# Create data.txt of files in $path
finder = PathFinder.PathFinder()
finder.GetDict(path)

# Read previously created dictionary into $data
json_data = open('data.txt').read()
data = json.loads(json_data)

artist_ids = {}
artists_not_found = []
albums_not_found = {}
deluxe_albums = {}

# Iterate through dictionary, first level is artist folders
for local_artist in data['children']:
    # Use artist name to find artist_id
    input_artist = local_artist['name']
    artist_id = crawler.GetArtistID(input_artist, spotify_token)
    # If artist doesn't exist on Spotify, add to list and continue at next artist
    if artist_id == 0:
        artists_not_found.append(input_artist)
        continue

    # Artist exists and we have their $artist_id

    # Get all albums on Spotify
    albums_data = crawler.GetArtistAlbums(artist_id, spotify_token)
    # If the artist has no albums, continue at next artist
    if len(albums_data) < 1:
        continue

    # Get list of all album names on Spotify
    album_names = []
    for album in albums_data['items']:
        album_names.append(album['name'])
    # Iterate through dictionary, second level is album folders
    for local_album in local_artist['children']:
        input_album = local_album['name']
        if not any(input_album in s for s in album_names):
            if "Deluxe" in input_album:
                deluxe_albums[input_artist] = input_album
            albums_not_found[input_artist] = input_album
    # Now have a list of all local albums not found on Spotify

with open('artists.txt', 'w') as outfile:
    json.dump(artists_not_found, outfile, indent=4)

with open('albums.txt', 'w') as outfile:
    json.dump(albums_not_found, outfile, indent=4)

print(deluxe_albums)