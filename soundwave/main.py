import os
import glob
import tkinter as tk
from gui.main_window import MainWindow
from core.music_libary import MusicLibrary, Music
from player.strategies import SequentialStrategy
from player.player import Player
from core.history import HistoryStack
from core.playlist import PlaylistManager
from data.storage import load_all_data


def load_musics_from_assets():
    """
    Carrega todos os arquivos .mp3 da pasta 'assets' e cria objetos Music para cada um.

    Returns:
        list[Music]: Lista de objetos Music carregados dos arquivos .mp3.
    """
    musics = []
    mp3_files = glob.glob("assets/*.mp3")
    for file_path in mp3_files:
        filename = os.path.basename(file_path)
        title = os.path.splitext(filename)[0]
        music = Music(
            title=title,
            album="",
            genre="",
            path=file_path
        )
        musics.append(music)
    return musics


def main():
    """
    Função principal que carrega os dados, inicializa os objetos principais do sistema e inicia a interface gráfica.
    """
    # Carrega biblioteca e playlists salvas (se existirem)
    library, playlist_manager, history = load_all_data()

    # Inicializa a biblioteca e gerenciador de playlists caso não existam
    if library is None:
        library = MusicLibrary()
    if playlist_manager is None:
        playlist_manager = PlaylistManager()
    if history is None:
        history = HistoryStack()


    # Adiciona músicas da pasta 'assets' à biblioteca (se ainda não estiverem presentes)
    for music in load_musics_from_assets():
        if not any(m.path == music.path for m in library.in_order_list()):
            library.insert(music)

    # Cria o player com estratégia sequencial e histórico
    player = Player(SequentialStrategy(), history)

    # Inicializa a interface gráfica principal
    root = tk.Tk()
    root.title("SoundWave Player")
    app = MainWindow(root, player, library, playlist_manager, history)
    root.mainloop()


if __name__ == "__main__":
    main()
