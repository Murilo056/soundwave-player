import random


class PlaybackStrategy:
    """Classe base para estratégias de reprodução."""

    def play_next(self, queue):
        """Define a lógica de seleção da próxima música."""
        raise NotImplementedError("Subclasses devem implementar este método.")


class SequentialStrategy(PlaybackStrategy):
    """Reprodução sequencial: próxima música é a próxima da fila."""

    def play_next(self, queue):
        return queue.pop(0) if queue else None


class ShuffleStrategy(PlaybackStrategy):
    """Reprodução aleatória: escolhe uma música aleatória da fila."""

    def play_next(self, queue):
        if queue:
            index = random.randint(0, len(queue) - 1)
            return queue.pop(index)
        return None
