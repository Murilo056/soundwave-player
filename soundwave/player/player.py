import pygame
from threading import Thread
import time


class Player:
    """
    Classe principal de controle de reprodução de músicas.
    Utiliza pygame para tocar arquivos .mp3.
    """

    def __init__(self, strategy, history):
        pygame.mixer.init()
        self.queue = []
        self.current_index = -1
        self.current = None
        self.strategy = strategy
        self.history = history
        self.running = False
        self.paused = False
        self._thread = None

    def set_strategy(self, strategy):
        """Define a estratégia de reprodução (sequencial, shuffle etc.)."""
        self.strategy = strategy

    def add_to_queue(self, music):
        """Adiciona uma música à fila de reprodução."""
        self.queue.append(music)

    def play(self, on_change_callback=None):
        """Inicia a reprodução da fila de músicas."""
        if not self.queue or self.running:
            return

        if self.current_index == -1:
            self.current_index = 0

        def _play():
            self.running = True
            while self.current_index < len(self.queue) and self.running:
                self.current = self.queue[self.current_index]
                try:
                    pygame.mixer.music.load(self.current.path)
                    pygame.mixer.music.play()
                    if on_change_callback:
                        on_change_callback(self.current)

                    while self.running:
                        if self.paused:
                            time.sleep(0.5)
                            continue
                        if not pygame.mixer.music.get_busy():
                            break
                        time.sleep(0.5)

                    if self.running:
                        self.current_index += 1
                except Exception as e:
                    print(f"Erro ao tocar música: {e}")
                    self.current_index += 1
            self.running = False

        self._thread = Thread(target=_play, daemon=True)
        self._thread.start()

    def stop(self):
        """Para a reprodução da música atual."""
        self.running = False
        pygame.mixer.music.stop()
        if self._thread:
            self._thread.join(timeout=1)

    def pause(self):
        """Pausa a reprodução."""
        pygame.mixer.music.pause()
        self.paused = True

    def unpause(self):
        """Retoma a reprodução pausada."""
        pygame.mixer.music.unpause()
        self.paused = False

    def next(self, on_change_callback=None):
        """Avança para a próxima música da fila."""
        if self.current_index + 1 < len(self.queue):
            self.stop()
            self.current_index += 1
            self.play(on_change_callback)
        else:
            print("Fim da fila.")

    def previous(self, on_change_callback=None):
        """Volta para a música anterior da fila."""
        if self.current_index > 0:
            self.stop()
            self.current_index -= 1
            self.play(on_change_callback)
        else:
            print("Início da fila.")
