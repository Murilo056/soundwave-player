import os
import pickle

# Caminhos padrão dos arquivos de dados
LIBRARY_FILE = 'data/library.pkl'
PLAYLISTS_FILE = 'data/playlists.pkl'
HISTORY_FILE = 'data/history.pkl'


class StorageManager:
    """
    Classe utilitária para salvar e carregar dados persistentes do sistema:
    biblioteca de músicas, playlists e histórico.
    """

    @staticmethod
    def save_library(library):
        """Salva a biblioteca de músicas em disco."""
        os.makedirs('data', exist_ok=True)
        with open(LIBRARY_FILE, 'wb') as f:
            pickle.dump(library, f)

    @staticmethod
    def load_library():
        """Carrega a biblioteca de músicas do disco."""
        if os.path.exists(LIBRARY_FILE):
            with open(LIBRARY_FILE, 'rb') as f:
                return pickle.load(f)
        return None

    @staticmethod
    def save_playlists(playlist_manager):
        """Salva todas as playlists em disco."""
        os.makedirs('data', exist_ok=True)
        with open(PLAYLISTS_FILE, 'wb') as f:
            pickle.dump(playlist_manager, f)

    @staticmethod
    def load_playlists():
        """Carrega as playlists do disco."""
        if os.path.exists(PLAYLISTS_FILE):
            with open(PLAYLISTS_FILE, 'rb') as f:
                return pickle.load(f)
        return None

    @staticmethod
    def save_history(history):
        """Salva o histórico de músicas tocadas em disco."""
        os.makedirs('data', exist_ok=True)
        with open(HISTORY_FILE, 'wb') as f:
            pickle.dump(history, f)

    @staticmethod
    def load_history():
        """Carrega o histórico de músicas do disco."""
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'rb') as f:
                return pickle.load(f)
        return None


def load_all_data():
    """
    Carrega a biblioteca e playlists simultaneamente.
    Retorna uma tupla: (biblioteca, playlists)
    """
    library = StorageManager.load_library()
    playlists = StorageManager.load_playlists()
    return library, playlists
