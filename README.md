```markdown
# 📥 Baixador do YouTube (YouTube Downloader)

Uma aplicação desktop moderna, leve e intuitiva para baixar vídeos e extrair áudios do YouTube com qualidade. Desenvolvida em Python utilizando **CustomTkinter** para a interface gráfica e **yt-dlp** para o processamento de media.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-blueviolet?style=for-the-badge)
![yt-dlp](https://img.shields.io/badge/Engine-yt--dlp-red?style=for-the-badge)

---

## ✨ Funcionalidades

* **Download de Vídeos (MP4):** Suporte a resoluções até 1080p (Full HD)[cite: 2].
* **Conversão de Áudio (MP3):** Extração de áudio em alta qualidade (192kbps)[cite: 2].
* **Interface Moderna:** Tema adaptativo (Dark/Light Mode) conforme as configurações do teu sistema[cite: 2].
* **Execução em Segundo Plano:** Processamento em *threads* separadas para impedir que a janela da aplicação congele durante os downloads[cite: 2].
* **Log em Tempo Real:** Acompanhamento do progresso e velocidade do download em tempo real[cite: 2].

---

## 🛠️ Tecnologias Utilizadas

* **[Python](https://www.python.org/):** Linguagem principal do projeto.
* **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter):** Biblioteca para a interface gráfica de utilizador (GUI)[cite: 2].
* **[yt-dlp](https://github.com/yt-dlp/yt-dlp):** Biblioteca para o motor de download de media[cite: 2].
* **[FFmpeg](https://ffmpeg.org/):** Necessário para a conversão e extração de áudio em formato MP3[cite: 2].

---

## 🚀 Como Executar o Projetos Localmente

### Pré-requisitos
Certifica-te de que tens o **Python 3.10+** e o **FFmpeg** instalados na tua máquina.

### Passos:
1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/NGCGet/BaixarConteudo.git](https://github.com/NGCGet/BaixarConteudo.git)
   cd BaixarConteudo/Youtube

```

2. **Instalar as dependências:**
```bash
pip install customtkinter yt-dlp

```


3. **Executar a aplicação:**
```bash
python __main__.py

```



---

## 📦 Gerar o Executável (.exe)

Caso queiras compilar o projeto e gerar um ficheiro `.exe` portátil utilizando o **PyInstaller**:

1. Instala o PyInstaller:
```bash
pip install pyinstaller

```


2. Executa o comando de compilação:
```bash
pyinstaller --onefile --noconsole --collect-all customtkinter --icon=meu_icone.ico __main__.py

```


3. O teu executável estará disponível dentro da pasta **`dist/`**.
