import os

class PathFinder:

    def GetFilePathList(self, FilePath):
        return self._makeFilePathList(FilePath)

    def GetArtistFromPath(self, FilePath):
        dirs = FilePath.split("\\")
        return dirs[1]

    def GetAlbumFromPath(self, FilePath):
        dirs = FilePath.split("\\")
        return dirs[2]

    def GetSongFromPath(self, FilePath):
        dirs = FilePath.split("\\")
        return dirs[-1]

    def _makeFilePathList(self, FilePath):
        list = []
        for path, dirs, files in os.walk(FilePath):
            if files:
                for song in files:
                    list.append(path + "\\" + song)
        return list


