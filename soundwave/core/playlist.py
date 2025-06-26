class Playlist:
    """
    Representa uma playlist de músicas.
    """

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, music):
        """Adiciona uma música à playlist (se ainda não existir)."""
        if music not in self.songs:
            self.songs.append(music)

    def remove_song(self, music):
        """Remove uma música da playlist."""
        if music in self.songs:
            self.songs.remove(music)

    def move_song(self, from_index, to_index):
        """Move uma música de uma posição para outra na playlist."""
        if 0 <= from_index < len(self.songs) and 0 <= to_index < len(self.songs):
            song = self.songs.pop(from_index)
            self.songs.insert(to_index, song)


class PlaylistManager:
    """
    Gerencia múltiplas playlists no sistema.
    """

    def __init__(self):
        self.playlists = {}

    def create_playlist(self, name):
        """Cria uma nova playlist com o nome fornecido."""
        if name not in self.playlists:
            self.playlists[name] = Playlist(name)

    def delete_playlist(self, name):
        """Exclui a playlist com o nome fornecido."""
        if name in self.playlists:
            del self.playlists[name]

    def rename_playlist(self, old_name, new_name):
        """Renomeia uma playlist existente."""
        if old_name in self.playlists and new_name not in self.playlists:
            playlist = self.playlists[old_name]
            playlist.name = new_name
            self.playlists[new_name] = playlist
            del self.playlists[old_name]

    def get_playlist(self, name):
        """Retorna a playlist com o nome fornecido."""
        return self.playlists.get(name)

    def list_playlists(self):
        """Retorna uma lista com os nomes de todas as playlists."""
        return list(self.playlists.keys())
