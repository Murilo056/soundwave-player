class Command:
    """Classe base para comandos executáveis no player."""

    def execute(self):
        raise NotImplementedError("Subclasses devem implementar este método.")


class PlayCommand(Command):
    """Comando para iniciar a reprodução."""

    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.play()


class StopCommand(Command):
    """Comando para parar a reprodução."""

    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.stop()


class PauseCommand(Command):
    """Comando para pausar a reprodução."""

    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.pause()


class NextCommand(Command):
    """Comando para avançar para a próxima música."""

    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.stop()
        self.player.play()


class PreviousCommand(Command):
    """Comando para voltar para a música anterior."""

    def __init__(self, player, history):
        self.player = player
        self.history = history

    def execute(self):
        self.player.stop()
        prev_music = self.history.pop()
        if prev_music:
            self.player.add_to_queue(prev_music)
            self.player.play()
