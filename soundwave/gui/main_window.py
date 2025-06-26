import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from core.music_libary import Music
from data.storage import StorageManager
import pygame
import os
import shutil


class MainWindow:
    """
    Classe responsável por controlar a interface principal do SoundWave Player.
    """

    def __init__(self, root, player, library, playlist_manager, history):
        self.root = root
        self.player = player
        self.library = library
        self.playlist_manager = playlist_manager
        self.history = history
        self.is_paused = False
        self.current_playlist = None
        self.last_clicked = 'library'

        self.root.configure(bg="#121212")
        self.root.title("🎵 SoundWave Player")

        self.current_label = tk.Label(
            root, text="Nenhuma música tocando", fg="#eeeeee",
            bg="#121212", font=("Arial", 12, "bold")
        )
        self.current_label.grid(row=0, column=0, columnspan=3, pady=(10, 5))

        # Cria títulos e listas principais
        self._create_list_title("🎼 Biblioteca", 0)
        self._create_list_title("🎵 Músicas da Playlist", 1)
        self._create_list_title("🕘 Histórico", 2)

        self.listbox = self._create_listbox(0)
        self.playlist_songs_listbox = self._create_listbox(1)
        self.history_listbox = self._create_listbox(2)

        self.load_library_to_listbox()
        self._create_controls()
        self.setup_playlist_ui()

    def _create_list_title(self, text, column):
        """Cria o título acima de cada listbox."""
        label = tk.Label(
            self.root, text=text, fg="#eeeeee", bg="#121212",
            font=("Arial", 11, "bold")
        )
        label.grid(row=1, column=column, pady=(5, 0))

    def _create_listbox(self, column):
        """Cria e configura uma listbox."""
        box = tk.Listbox(
            self.root, width=50, height=18, exportselection=False,
            font=("Courier New", 10), bg="#1f1f1f", fg="#eeeeee",
            selectbackground="#8a4fff", selectforeground="#ffffff",
            relief=tk.FLAT, bd=0
        )
        box.grid(row=2, column=column, padx=10, pady=5)
        if column == 0:
            box.bind("<Button-1>", lambda e: self.set_last_clicked('library'))
        return box

    def _create_controls(self):
        """Cria os botões de controle principais da interface."""
        frame = tk.Frame(self.root, bg="#121212")
        frame.grid(row=3, column=0, columnspan=3, pady=(10, 10))

        button_cfg = {
            "padx": 15, "pady": 8, "bg": "#6a3ea1", "fg": "white",
            "relief": tk.FLAT, "width": 16, "font": ("Arial", 9, "bold"),
            "activebackground": "#9b6ffb", "activeforeground": "white",
            "bd": 0,
            "highlightthickness": 0,
            "cursor": "hand2"
        }

        btns = [
            ("➕ Adicionar Música", self.add_music),
            ("▶ Reproduzir", self.play),
            ("⏹ Parar", self.stop),
            ("⏸ Pausar", self.toggle_pause),
            ("⏭ Próxima", self.next),
            ("⏮ Voltar", self.previous),
            ("❤️ Favoritar/Desfavoritar", self.toggle_favorite),
            ("⭐ Mostrar Favoritas", self.show_favorites),
            ("📂 Mostrar Todas", self.load_library_to_listbox),
        ]

        for idx, (text, cmd) in enumerate(btns):
            btn = tk.Button(frame, text=text, command=cmd, **button_cfg)
            btn.grid(row=0, column=idx, padx=4)
            if text == "⏸ Pausar":
                self.pause_button = btn

        tk.Label(frame, text="🔊 Volume", bg="#121212", fg="#eeeeee").grid(row=1, column=0, sticky="w", padx=4)
        self.volume_scale = tk.Scale(
            frame, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume,
            bg="#1f1f1f", fg="#eeeeee", troughcolor="#8a4fff",
            highlightthickness=0, bd=0, sliderrelief=tk.FLAT, width=12
        )
        self.volume_scale.set(50)
        self.volume_scale.grid(row=1, column=1, columnspan=3, sticky="we", padx=10)

    def set_last_clicked(self, source):
        """Registra qual seção foi clicada por último (biblioteca ou playlist)."""
        self.last_clicked = source

    def set_volume(self, value):
        """Define o volume de reprodução."""
        try:
            pygame.mixer.music.set_volume(int(value) / 100)
        except Exception as e:
            print("Erro ao ajustar volume:", e)

    def load_library_to_listbox(self):
        """Carrega todas as músicas da biblioteca na listbox."""
        self.listbox.delete(0, tk.END)
        vistos = set()
        for music in self.library.in_order_list():
            if music.path not in vistos:
                vistos.add(music.path)
                display = str(music) + (" ❤️" if getattr(music, "is_favorite", False) else "")
                self.listbox.insert(tk.END, display)

    def load_history_to_listbox(self):
        """Carrega o histórico de músicas tocadas na listbox."""
        self.history_listbox.delete(0, tk.END)
        for music in reversed(self.history.stack):
            self.history_listbox.insert(tk.END, str(music))

    def setup_playlist_ui(self):
        """Cria a interface gráfica de gerenciamento de playlists."""
        frame = tk.Frame(self.root, bg="#121212", padx=10, pady=10)
        frame.grid(row=4, column=0, columnspan=3, sticky="we")

        left_frame = tk.Frame(frame, bg="#121212")
        left_frame.pack(side=tk.LEFT)

        tk.Label(
            left_frame, text="📁 Playlists", fg="#eeeeee",
            bg="#121212", font=("Arial", 10, "bold")
        ).pack(pady=(0, 2))

        self.playlist_listbox = tk.Listbox(
            left_frame, width=30, exportselection=False,
            font=("Courier", 10), bg="#1f1f1f", fg="#eeeeee",
            selectbackground="#8a4fff", selectforeground="#ffffff", relief=tk.FLAT, bd=0
        )
        self.playlist_listbox.pack()
        self.playlist_listbox.bind('<<ListboxSelect>>', self.on_playlist_select)
        self.playlist_listbox.bind('<Button-1>', lambda e: self.set_last_clicked('playlist'))

        btn_frame = tk.Frame(frame, bg="#121212")
        btn_frame.pack(side=tk.LEFT, padx=15)

        btn_data = [
            ("➕ Nova Playlist", self.create_playlist),
            ("🗑 Excluir Playlist", self.delete_playlist),
            ("➕ Música na Playlist", self.add_song_to_playlist),
            ("➖ Remover da Playlist", self.remove_song_from_playlist),
            ("🔼 Subir Música", self.move_song_up),
            ("🔽 Descer Música", self.move_song_down)
        ]

        for text, cmd in btn_data:
            tk.Button(
                btn_frame, text=text, command=cmd, width=25,
                bg="#6a3ea1", fg="white", relief=tk.FLAT,
                activebackground="#9b6ffb", activeforeground="white",
                bd=0, highlightthickness=0, cursor="hand2"
            ).pack(pady=2)

        self.refresh_playlists()

    def refresh_playlists(self):
        """Atualiza a listagem de playlists."""
        self.playlist_listbox.delete(0, tk.END)
        for name in self.playlist_manager.list_playlists():
            self.playlist_listbox.insert(tk.END, name)

    def on_playlist_select(self, _):
        """Atualiza músicas da playlist selecionada."""
        selection = self.playlist_listbox.curselection()
        if not selection:
            self.current_playlist = None
            self.playlist_songs_listbox.delete(0, tk.END)
            return
        name = self.playlist_listbox.get(selection[0])
        self.current_playlist = self.playlist_manager.get_playlist(name)
        self.refresh_playlist_songs()

    def refresh_playlist_songs(self):
        """Carrega músicas da playlist selecionada."""
        self.playlist_songs_listbox.delete(0, tk.END)
        if self.current_playlist:
            for song in self.current_playlist.songs:
                self.playlist_songs_listbox.insert(tk.END, str(song))

    def create_playlist(self):
        """Cria uma nova playlist com nome informado pelo usuário."""
        name = simpledialog.askstring("Nova Playlist", "Nome:")
        if name:
            self.playlist_manager.create_playlist(name)
            StorageManager.save_playlists(self.playlist_manager)
            self.refresh_playlists()

    def delete_playlist(self):
        """Exclui a playlist selecionada, se houver."""
        selection = self.playlist_listbox.curselection()
        if not selection:
            return
        name = self.playlist_listbox.get(selection[0])
        if messagebox.askyesno("Excluir", f"Excluir playlist '{name}'?"):
            self.playlist_manager.delete_playlist(name)
            StorageManager.save_playlists(self.playlist_manager)
            self.refresh_playlists()
            self.playlist_songs_listbox.delete(0, tk.END)
            self.current_playlist = None

    def add_song_to_playlist(self):
        """Adiciona música da biblioteca à playlist selecionada."""
        if not self.current_playlist:
            messagebox.showwarning("Playlist", "Selecione uma playlist.")
            return
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Música", "Selecione uma música.")
            return
        music_str = self.listbox.get(selection[0]).replace(" ❤️", "")
        music = next((m for m in self.library.in_order_list() if str(m) == music_str), None)
        if music:
            self.current_playlist.add_song(music)
            StorageManager.save_playlists(self.playlist_manager)
            self.refresh_playlist_songs()

    def remove_song_from_playlist(self):
        """Remove música selecionada da playlist."""
        if not self.current_playlist:
            return
        selection = self.playlist_songs_listbox.curselection()
        if not selection:
            return
        song = self.current_playlist.songs[selection[0]]
        self.current_playlist.remove_song(song)
        StorageManager.save_playlists(self.playlist_manager)
        self.refresh_playlist_songs()

    def move_song_up(self):
        """Move a música selecionada para cima na playlist."""
        if not self.current_playlist:
            return
        i = self.playlist_songs_listbox.curselection()
        if i and i[0] > 0:
            self.current_playlist.move_song(i[0], i[0] - 1)
            StorageManager.save_playlists(self.playlist_manager)
            self.refresh_playlist_songs()
            self.playlist_songs_listbox.select_set(i[0] - 1)

    def move_song_down(self):
        """Move a música selecionada para baixo na playlist."""
        if not self.current_playlist:
            return
        i = self.playlist_songs_listbox.curselection()
        if i and i[0] < len(self.current_playlist.songs) - 1:
            self.current_playlist.move_song(i[0], i[0] + 1)
            StorageManager.save_playlists(self.playlist_manager)
            self.refresh_playlist_songs()
            self.playlist_songs_listbox.select_set(i[0] + 1)

    def add_music(self):
        """Adiciona nova música à biblioteca a partir do sistema de arquivos."""
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            filename = os.path.basename(file_path)
            assets_path = os.path.join("assets", filename)
            os.makedirs("assets", exist_ok=True)
            if not os.path.exists(assets_path):
                shutil.copy(file_path, assets_path)
            title = filename.replace(".mp3", "")
            if not any(m.path == assets_path for m in self.library.in_order_list()):
                music = Music(title, "", "", assets_path)
                self.library.insert(music)
                StorageManager.save_library(self.library)
                self.player.add_to_queue(music)
                self.load_library_to_listbox()

    def play(self):
        """Executa a reprodução da playlist ou biblioteca."""
        def on_change(music):
            self.root.after(0, lambda: self.update_label(music))
            self.is_paused = False
            self.pause_button.config(text="⏸ Pausar")

        self.player.queue.clear()
        songs = (
            self.current_playlist.songs
            if self.last_clicked == 'playlist' and self.current_playlist
            else self.library.in_order_list()
        )
        for music in songs:
            self.player.add_to_queue(music)
        self.player.play(on_change_callback=on_change)

    def stop(self):
        """Para a reprodução atual."""
        self.player.stop()
        self.current_label.config(text="Reprodução parada")
        self.is_paused = False
        self.pause_button.config(text="⏸ Pausar")

    def toggle_pause(self):
        """Alterna entre pausar e continuar a reprodução."""
        if self.is_paused:
            self.player.unpause()
            self.pause_button.config(text="⏸ Pausar")
            self.current_label.config(text=f"Tocando agora: {self.player.current}")
            self.is_paused = False
        else:
            self.player.pause()
            self.pause_button.config(text="▶ Continuar")
            self.current_label.config(text="Reprodução pausada")
            self.is_paused = True

    def next(self):
        """Avança para a próxima música."""
        def on_change(music):
            self.root.after(0, lambda: self.update_label(music))
            self.is_paused = False
            self.pause_button.config(text="⏸ Pausar")
            self.history.push(music)
            StorageManager.save_history(self.history)
            self.load_history_to_listbox()

        self.player.next(on_change_callback=on_change)

    def previous(self):
        """Volta para a música anterior."""
        def on_change(music):
            self.root.after(0, lambda: self.update_label(music))
            self.is_paused = False
            self.pause_button.config(text="⏸ Pausar")
            self.history.push(music)
            StorageManager.save_history(self.history)
            self.load_history_to_listbox()

        self.player.previous(on_change_callback=on_change)

    def toggle_favorite(self):
        """Marca ou desmarca uma música como favorita."""
        selection = self.listbox.curselection()
        if not selection:
            return
        raw = self.listbox.get(selection[0]).replace(" ❤️", "").strip()
        for m in self.library.in_order_list():
            if m.title == raw:
                m.is_favorite = not getattr(m, "is_favorite", False)
                StorageManager.save_library(self.library)
                self.load_library_to_listbox()
                return
        messagebox.showerror("Erro", "Música não encontrada.")

    def show_favorites(self):
        """Exibe apenas as músicas marcadas como favoritas."""
        self.listbox.delete(0, tk.END)
        for m in self.library.in_order_list():
            if getattr(m, "is_favorite", False):
                self.listbox.insert(tk.END, str(m) + " ❤️")

    def update_label(self, music):
        """Atualiza o rótulo da música atual."""
        self.current_label.config(text=f"Tocando agora: {music}")
