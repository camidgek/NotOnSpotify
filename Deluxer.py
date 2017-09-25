import SpotifyAPI
import os
import re
import shutil


class Deluxer:

    crawler = SpotifyAPI.SpotifyAPI()
    changed_albums = {}

    def FixLibrary(self, p_path_library, p_spotify_token):
        # Iterate through artists in library
        for local_artist in os.listdir(p_path_library):
            # Create path into artist folders and pass to self.FixArtist
            path_artist = p_path_library + "\\" + local_artist
            self.FixArtist(path_artist, p_spotify_token)

    def FixArtist(self, p_path_artist, p_spotify_token):
        # Create list of albums inside artist folder
        local_albums = os.listdir(p_path_artist)
        # Get index of each album with 'Deluxe' in the title
        indices = [i for i, local_album in enumerate(local_albums) if 'Deluxe' in local_album]
        if len(indices) > 0:
            for index in indices:
                path_album = p_path_artist + "\\" + local_albums[index]
                self.FixDeluxeAlbum(path_album, p_spotify_token)

    def FixDeluxeAlbum(self, p_path_album, p_spotify_token):
        local_artist = re.split(r'[\\]', p_path_album)[-2]
        local_album = re.split(r'[\\]', p_path_album)[-1]
        base_album = local_album.split(" (Deluxe", 1)[0]
        artist_id = self.crawler.GetArtistIDFromSearch(local_artist, p_spotify_token)
        sp_albums = self.crawler.GetAlbumsFromArtistID(artist_id, p_spotify_token)
        for sp_album in sp_albums:
            # If $sp_album is the Spotify Deluxe version of the $base_album and the $local_album is not already the same
            if base_album in sp_album['name'] and 'Deluxe' in sp_album['name'] and local_album != sp_album['name']:
                # Change the $local_album to be the Spotify Deluxe version
                self.changed_albums[local_album] = sp_album['name']
                path_album_new = "\\".join(re.split(r'[\\]', p_path_album)[:-1]) + "\\" + sp_album['name']
                shutil.move(p_path_album, path_album_new)
                return


token = "BQAxuZmnG_bUWYiHWVNOUCr-8EXzCCvmkvdWcvAnEtKqBYNHwbwN3uP54AQjGntBJ2RcgF4juzXTOs6pUNsh6ABTX5jvE0rriI7bVkNspKwS_tJR73UDlz4d3K2knDcp2VCBnuHvsQ83RI-7"
path = os.path.abspath('test')
deluxer = Deluxer()
deluxer.FixLibrary(path, token)
print(deluxer.changed_albums)