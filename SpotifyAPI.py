import requests


class SpotifyAPI:

    def GetArtistID(self, p_artist, p_spotify_token):
        # Create the API request
        request_query = p_artist.replace(" ", "+")
        request_url = 'https://api.spotify.com/v1/search?q=' + request_query + '&type=artist'
        request_header = {'Accept': 'application/json',
                          'Authorization': 'Bearer ' + p_spotify_token}
        # Send request, get $response, and convert from json to dictionary
        response = requests.get(request_url, headers=request_header)
        json_artist_data = response.json()
        artist_data = json_artist_data['artists']['items']
        # Check if artist exists
        if len(artist_data) > 0:
            # If artist exists, return the $artist_id of the first matching artist
            for artist in artist_data:
                if artist['name'] == p_artist:
                    artist_url = artist['external_urls']['spotify']
                    return artist_url.split("artist/", 1)[1]
        else:
            # If the artist doesn't exist, return 0
            return 0

    def GetArtistAlbums(self, p_artist_id, p_spotify_token):
        # Create the API request
        request_url = 'https://api.spotify.com/v1/artists/' + p_artist_id + '/albums'
        request_header = {'Accept': 'application/json',
                          'Authorization': 'Bearer ' + p_spotify_token}
        # Send request, get $response, return as dictionary
        response = requests.get(request_url, headers=request_header)
        return response.json()

    def FixDeluxeAlbum(self, p_album, p_spotify_token):
        base_album = p_album.split(" (", 1)[0]
        request_query = base_album.replace(" ", "+")
        request_url = 'https://api.spotify.com/v1/search?q=' + request_query + '&type=album'
        request_header = {'Accept': 'application/json',
                          'Authorization': 'Bearer ' + p_spotify_token}
        # Send request, get $response, and convert from json to dictionary
        response = requests.get(request_url, headers=request_header)
        json_album_data = response.json()
        album_data = json_album_data['albums']['items']
        for album in album_data:
            if base_album in album['name'] and 'Deluxe' in album['name']:
                return album['name']
        return p_album
