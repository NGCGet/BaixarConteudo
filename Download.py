import threading
import customtkinter as ctk
import yt_dlp

# Configuração do tema do CustomTkinter
ctk.set_appearance_mode('System')  # Segue o tema do sistema (Dark/Light)
ctk.set_default_color_theme('blue')  # Cor de destaque


class YouTubeDownloaderApp(ctk.CTk):

  def __init__(self):
    super().__init__()

    self.title('YouTube Downloader - yt-dlp')
    self.geometry('550x460')
    self.resizable(False, False)

    # Título da Aplicação
    self.titulo_label = ctk.CTkLabel(
        self, text='Baixador do YouTube', font=('Arial', 22, 'bold')
    )
    self.titulo_label.pack(pady=20)

    # Campo de URL
    self.url_label = ctk.CTkLabel(
        self, text='Cole o link do vídeo:', font=('Arial', 14)
    )
    self.url_label.pack(anchor='w', padx=40)

    self.url_entry = ctk.CTkEntry(
        self,
        placeholder_text='https://www.youtube.com/watch?v=...',
        width=470,
        height=40,
    )
    self.url_entry.pack(pady=5, padx=40)

    # Menu de Seleção de Formato
    self.formato_label = ctk.CTkLabel(
        self, text='Escolha o formato de saída:', font=('Arial', 14)
    )
    self.formato_label.pack(anchor='w', padx=40, pady=(10, 0))

    self.formato_var = ctk.StringVar(value='Vídeo MP4 (Full HD / 1080p)')
    self.formato_menu = ctk.CTkOptionMenu(
        self,
        values=['Vídeo MP4 (Full HD / 1080p)', 'Áudio MP3 (192kbps)'],
        variable=self.formato_var,
        width=470,
        height=35,
    )
    self.formato_menu.pack(pady=5, padx=40)

    # Botão de Download
    self.btn_baixar = ctk.CTkButton(
        self,
        text='Iniciar Download',
        command=self.iniciar_download_thread,
        height=42,
        font=('Arial', 14, 'bold'),
    )
    self.btn_baixar.pack(pady=20, padx=40)

    # Caixa de Texto (Log / Progresso)
    self.status_textbox = ctk.CTkTextbox(
        self, width=470, height=110, font=('Consolas', 11)
    )
    self.status_textbox.pack(pady=(0, 20), padx=40)
    self.status_textbox.insert('0.1', 'Pronto para baixar...\n')
    self.status_textbox.configure(state='disabled')

  def log(self, mensagem):
    """Atualiza a caixa de texto de status de forma segura."""
    self.status_textbox.configure(state='normal')
    self.status_textbox.insert('end', mensagem + '\n')
    self.status_textbox.see('end')
    self.status_textbox.configure(state='disabled')

  def iniciar_download_thread(self):
    """Inicia o processo em segundo plano para não travar a janela."""
    url = self.url_entry.get().strip()
    if not url:
      self.log('⚠️ Erro: Por favor, insira um link válido!')
      return

    self.btn_baixar.configure(state='disabled', text='Baixando...')

    # Dispara a thread de download
    threading.Thread(
        target=self.executar_download, args=(url,), daemon=True
    ).start()

  def executar_download(self, url):
    formato = self.formato_var.get()

    def progress_hook(d):
      if d['status'] == 'downloading':
        porcentagem = d.get('_percent_str', '0.0%').strip()
        velocidade = d.get('_speed_str', 'N/A').strip()
        self.log(f'Baixando: {porcentagem} | Velocidade: {velocidade}')

    try:
      if 'MP4' in formato:
        ydl_opts = {
            'format': (
                'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best'
            ),
            'outtmpl': '%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],
        }
        self.log('\n[+] Iniciando download do vídeo (MP4)...')
      else:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }
            ],
            'outtmpl': '%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],
        }
        self.log('\n[+] Iniciando download e conversão para MP3...')

      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

      self.log('\n✅ Download concluído com sucesso!')
    except Exception as e:
      self.log(f'\n❌ Erro: {e}')
    finally:
      # Reativa o botão após o término
      self.btn_baixar.configure(state='normal', text='Iniciar Download')