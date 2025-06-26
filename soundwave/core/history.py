class HistoryStack:
    """
    Estrutura de pilha para armazenar o histórico de músicas reproduzidas.
    """

    def __init__(self):
        self.stack = []

    def push(self, music):
        """Adiciona uma música ao topo do histórico."""
        self.stack.append(music)

    def pop(self):
        """Remove e retorna a última música do histórico, se existir."""
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        """Retorna a última música do histórico sem removê-la."""
        if self.stack:
            return self.stack[-1]
        return None

    def is_empty(self):
        """Verifica se o histórico está vazio."""
        return len(self.stack) == 0

    def clear(self):
        """Limpa todo o histórico."""
        self.stack.clear()
