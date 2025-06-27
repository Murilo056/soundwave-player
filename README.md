🎵 SoundWave Player
SoundWave Player é um reprodutor de músicas em Python com interface gráfica construída em Tkinter. Ele permite a reprodução de arquivos .mp3, organização da biblioteca com playlists, histórico de reprodução e favoritos — tudo de forma simples, moderna e offline.

🖼️ Interface
🎼 Biblioteca: lista completa das músicas disponíveis

📁 Playlists: crie, edite e exclua playlists com músicas personalizadas

🕘 Histórico: visualize as últimas músicas tocadas

🎮 Controles: reproduzir, pausar, parar, avançar, retroceder, ajustar volume e favoritar músicas

📦 Requisitos
Python 3.12+

pygame (para reprodução de áudio)

Instale as dependências com:

bash
Copiar
Editar
pip install -r requirements.txt
▶️ Como Executar
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/Murilo056/soundwave-player.git
cd soundwave-player
Execute o projeto:

bash
Copiar
Editar
python main.py
⚙️ Funcionamento Importante
A reprodução alterna entre biblioteca ou playlist conforme o último clique do usuário:

Se não houver clique anterior, toca músicas variadas da biblioteca.

Se o último clique foi em uma playlist, toca apenas as músicas dessa playlist selecionada.

Para adicionar uma música a uma playlist:

Selecione a música na biblioteca.

Clique na playlist desejada.

Clique no botão + Música na playlist.

Para remover uma música da playlist:

Selecione a música dentro da lista de músicas da playlist e clique em Remover da playlist.

Para subir ou descer uma música dentro da playlist:

Selecione a música na lista da playlist e utilize os botões de mover para cima ou para baixo.

🧪 Como Rodar os Testes
Os testes estão na pasta tests/.

Execute todos os testes com:

bash
Copiar
Editar
python -m unittest discover -s tests
🛠️ Funcionalidades
🎧 Reproduzir músicas da biblioteca ou playlists

➕ Adicionar novas músicas (copiadas para a pasta assets/)

📝 Criar, editar e excluir playlists

💾 Salvamento automático de biblioteca, playlists e histórico

🔁 Avançar e voltar faixas

⏸ Pausar e continuar reprodução

⭐ Favoritar músicas e listar apenas favoritas

🔊 Controle de volume
