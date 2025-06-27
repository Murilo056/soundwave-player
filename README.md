# 🎵 SoundWave Player

**SoundWave Player** é um reprodutor de músicas em Python com interface gráfica construída em Tkinter.  
Ele permite a reprodução de arquivos `.mp3`, organização da biblioteca com playlists, histórico de reprodução e favoritos — tudo de forma simples, moderna e offline.

---

## 🖼️ Interface

- 🎼 **Biblioteca**  
  Lista completa das músicas disponíveis.

- 📁 **Playlists**  
  Crie, edite e exclua playlists com músicas personalizadas.

- 🕘 **Histórico**  
  Visualize as últimas músicas tocadas.

- 🎮 **Controles**  
  Reproduzir, pausar, parar, avançar, retroceder, ajustar volume e favoritar músicas.

---

## 📦 Requisitos

- Python 3.12 ou superior  
- Biblioteca `pygame` (para reprodução de áudio)

Para instalar as dependências, execute:

pip install -r requirements.txt

---

## ▶️ Como Executar

1. Clone o repositório:

git clone https://github.com/Murilo056/soundwave-player.git

2. Acesse a pasta do projeto;

3. Execute o player:

python main.py

---

## ⚙️ Funcionamento Importante

- O player alterna entre reproduzir músicas da **biblioteca** ou da **playlist** dependendo do último clique do usuário:

  - Se não houve clique anterior, o player toca músicas variadas da biblioteca.
  
  - Se o último clique foi numa playlist, o player toca apenas as músicas dessa playlist.

- **Para adicionar uma música a uma playlist:**

  1. Selecione a música na biblioteca.
  
  2. Clique na playlist desejada.
  
  3. Clique no botão **+ Música na playlist**.

- **Para remover uma música da playlist:**

  - Selecione a música na lista da playlist.
  
  - Clique no botão **Remover da playlist**.

- **Para ordenar músicas dentro da playlist:**

  - Selecione a música na lista da playlist.
  
  - Utilize os botões para mover a música para cima ou para baixo.

---

## 🧪 Como Rodar os Testes

Os testes automatizados estão localizados na pasta `soundwave/tests/` e cobrem funcionalidades principais como a biblioteca de músicas, histórico e integração com o player.

### 📦 Pré-requisitos

Certifique-se de estar na **raiz do projeto** e que o Python 3 esteja instalado corretamente.

### ▶️ Comando para executar todos os testes

```bash
python -m unittest discover -s soundwave/tests
```
---

## 🛠️ Funcionalidades

- 🎧 Reprodução de músicas da biblioteca ou playlists.

- ➕ Adição de novas músicas (copiadas para a pasta `assets/`).

- 📝 Criação, edição e exclusão de playlists.

- 💾 Salvamento automático da biblioteca, playlists e histórico.

- 🔁 Avançar e voltar faixas.

- ⏸ Pausar e continuar reprodução.

- ⭐ Favoritar músicas e listar apenas favoritas.

- 🔊 Controle de volume.
