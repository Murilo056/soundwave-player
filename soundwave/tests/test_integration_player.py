import unittest
from soundwave.core.music_libary import MusicLibrary, Music
from soundwave.core.history import HistoryStack
from soundwave.player.player import Player
from soundwave.player.strategies import SequentialStrategy
import time

class TestPlayerIntegration(unittest.TestCase):
    def setUp(self):
        self.library = MusicLibrary()
        self.history = HistoryStack()
        self.player = Player(SequentialStrategy(), self.history)

        self.music1 = Music("Teste 1", "", "", "assets/Charm - Anno Domini Beats.mp3")
        self.music2 = Music("Teste 2", "", "", "assets/tSweaty Linen - Surf Ninja 3.mp3")

        self.library.insert(self.music1)
        self.library.insert(self.music2)

    def test_play_and_history_flow(self):
        self.player.add_to_queue(self.music1)
        self.player.add_to_queue(self.music2)

        self.player.play()
        time.sleep(1)  # espera tocar um pouco

        self.assertTrue(self.player.running)
        self.assertIn(self.player.current, [self.music1, self.music2])

        self.player.stop()
        self.assertFalse(self.player.running)

if __name__ == "__main__":
    unittest.main()
