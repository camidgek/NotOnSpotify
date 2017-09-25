import requests


class SpotifyAPI:

    def GetArtistIDFromSearch(self, p_artist, p_spotify_token):
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

    def GetAlbumsFromArtistID(self, p_artist_id, p_spotify_token):
        # Create the API request
        request_url = 'https://api.spotify.com/v1/artists/' + p_artist_id + '/albums'
        request_header = {'Accept': 'application/json',
                          'Authorization': 'Bearer ' + p_spotify_token}
        # Send request, get $response, return as dictionary
        response = requests.get(request_url, headers=request_header)
        respone = response.json()
        return response.json()['items']

    def GetAlbumsFromSearch(self, p_album, p_spotify_token):
        request_query = p_album.replace(" ", "+")
        request_url = 'https://api.spotify.com/v1/search?q=' + request_query + '&type=album'
        request_header = {'Accept': 'application/json',
                          'Authorization': 'Bearer ' + p_spotify_token}
        # Send request, get $response, and convert from json to dictionary
        response = requests.get(request_url, headers=request_header)
        return response.json()['items']
