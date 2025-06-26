class Music:
    """
    Classe que representa uma música.
    """

    def __init__(self, title, album, genre, path):
        self.title = title
        self.album = album
        self.genre = genre
        self.path = path
        self.is_favorite = False  # Indica se é favorita

    def __str__(self):
        return f"{self.title}" + ("❤️" if self.is_favorite else "")


class MusicNode:
    """
    Nó da árvore binária de músicas.
    """

    def __init__(self, key, music: Music):
        self.key = key
        self.music = music
        self.left = None
        self.right = None


class MusicLibrary:
    """
    Biblioteca de músicas organizada em uma árvore binária de busca.
    """

    def __init__(self):
        self.root = None

    def insert(self, music: Music):
        """
        Insere uma música na árvore com base no título.
        """

        def _insert(node, key, music):
            if node is None:
                return MusicNode(key, music)
            if key < node.key:
                node.left = _insert(node.left, key, music)
            else:
                node.right = _insert(node.right, key, music)
            return node

        key = music.title.lower()
        self.root = _insert(self.root, key, music)

    def search(self, term):
        """
        Retorna uma lista de músicas cujo título contém o termo fornecido.
        """
        result = []

        def _search(node):
            if node is None:
                return
            if term.lower() in node.key:
                result.append(node.music)
            _search(node.left)
            _search(node.right)

        _search(self.root)
        return result

    def in_order_list(self):
        """
        Retorna todas as músicas da biblioteca em ordem alfabética.
        """
        result = []

        def _in_order(node):
            if node is None:
                return
            _in_order(node.left)
            result.append(node.music)
            _in_order(node.right)

        _in_order(self.root)
        return result
