import unittest
from soundwave.core.music_libary import MusicLibrary, Music

class TestMusicLibrary(unittest.TestCase):
    def setUp(self):
        self.library = MusicLibrary()
        self.music1 = Music("Música A", "", "", "path/a.mp3")
        self.music2 = Music("Música B", "", "", "path/b.mp3")

    def test_insert_and_in_order_list(self):
        self.library.insert(self.music1)
        self.library.insert(self.music2)
        result = self.library.in_order_list()
        self.assertEqual(len(result), 2)
        self.assertIn(self.music1, result)
        self.assertIn(self.music2, result)

    def test_search(self):
        self.library.insert(self.music1)
        results = self.library.search("a")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Música A")

if __name__ == '__main__':
    unittest.main()
