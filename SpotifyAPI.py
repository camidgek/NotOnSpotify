import requests
import secret

class SpotifyAPI:
    _clientID = "07281af1b6fe4be7b310550bf8cea3f9"
    _authEndpoint = "https://accounts.spotify.com/authorize"
    _tokenEndpoint = "https://accounts.spotify.com/api/token"
    _apiEndpoint = "https://api.spotify.com"
    _searchEndpoint = _apiEndpoint + "/v1/search"
    _artistEndpoint = _apiEndpoint + "/v1/artists/"

    def __init__(self):
        secret.getSecret()
        self._request_header = {'Accept': 'application/json',
                                'Authorization': 'Bearer ' + token}

    # def GetToken(self):
    #     client_string = self._client_id + ":" + self._client_secret
    #     auth_header = {'Authorization': "Basic " + base64.b64encode(client_string.encode('utf-8')).decode(),
    #                    'Content-Type': 'application/x-www-form-urlencoded'}
    #     auth_body = [('grant_type', 'client_credentials')]
    #     response = requests.post(self._token_endpoint, headers=auth_header, data=auth_body)
    #     return response.json()['access_token']

    def _requestAuthorization(self):
        request_query = "test"
        request_url = self._authEndpoint



    # def GetArtistIDFromSearch(self, p_artist):
    #     # Create the API request
    #     request_query = p_artist.replace(" ", "+")
    #     request_url = self._search_endpoint + '?q=' + request_query + '&type=artist'
    #     # Send request, get $response, and convert from json to dictionary
    #     response = requests.get(request_url, headers=self._request_header)
    #     json_artist_data = response.json()
    #     artist_data = json_artist_data['artists']['items']
    #     # Check if artist exists
    #     if len(artist_data) > 0:
    #         # If artist exists, return the $artist_id of the first matching artist
    #         for artist in artist_data:
    #             if artist['name'] == p_artist:
    #                 artist_url = artist['external_urls']['spotify']
    #                 return artist_url.split("artist/", 1)[1]
    #     else:
    #         # If the artist doesn't exist, return 0
    #         return 0
    #
    # def GetAlbumsFromArtistID(self, p_artist_id):
    #     # Create the API request
    #     request_url = self._artist_endpoint + p_artist_id + '/albums'
    #     # Send request, get $response, return as dictionary
    #     response = requests.get(request_url, headers=self._request_header)
    #     return response.json()['items']
    #
    # def GetAlbumsFromSearch(self, p_album):
    #     request_query = p_album.replace(" ", "+")
    #     request_url = self._search_endpoint + '?q=' + request_query + '&type=album'
    #     # Send request, get $response, and convert from json to dictionary
    #     response = requests.get(request_url, headers=self._request_header)
    #     return response.json()['items']
