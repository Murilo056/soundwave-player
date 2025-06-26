# 🎵 SoundWave Player

O **SoundWave Player** é um reprodutor de músicas em Python com interface gráfica construída em Tkinter. Ele permite a reprodução de arquivos `.mp3`, organização da biblioteca com playlists, histórico de reprodução e favoritos — tudo de forma simples, moderna e offline.

---

## 🖼️ Interface

- 🎼 Biblioteca: lista completa das músicas disponíveis
- 📁 Playlists: crie, edite e exclua playlists com músicas personalizadas
- 🕘 Histórico: visualize as últimas músicas tocadas
- 🎮 Controles: reproduzir, pausar, parar, avançar, retroceder, ajustar volume e favoritar músicas

---

## 📦 Requisitos

- Python 3.12+
- `pygame` (para reprodução de áudio)

Instale com:

```bash
pip install -r requirements.txt
```
---

#📁 Estrutura de Diretórios
soundwave/
├── assets/                # Arquivos .mp3
├── core/                 # Estruturas: biblioteca, histórico, playlist
│   ├── music_libary.py
│   ├── history.py
│   └── playlist.py
├── data/                 # Salvamento com pickle
│   └── storage.py
├── gui/
│   └── main_window.py    # Interface gráfica Tkinter
├── player/               # Estratégias de reprodução e lógica do player
│   ├── player.py
│   ├── strategies.py
│   └── commands.py
├── tests/                # Testes unitários e de integração
│   ├── test_music_library.py
│   └── test_integration_player.py
├── main.py               # Arquivo principal
├── requirements.txt

---

#▶️ Como Executar
git clone https://github.com/Murilo056/soundwave-player.git
cd soundwave-player

--

Instale os requisitos:
pip install -r requirements.txt

Execute o projeto:
python main.py
---

#🧪 Como Rodar os Testes
Os testes estão na pasta tests/.
Para executá-los: python -m unittest discover -s soundwave/tests

---
#🛠️ Funcionalidades
🎧 Reproduzir músicas da biblioteca ou de playlists

➕ Adicionar novas músicas (copiadas para a pasta assets)

📝 Criar e editar playlists

💾 Salvamento automático de biblioteca, playlists e histórico

🔁 Avançar / Voltar faixas

⏸ Pausar e continuar reprodução

⭐ Favoritar e listar apenas favoritas

🔊 Controle de volume
