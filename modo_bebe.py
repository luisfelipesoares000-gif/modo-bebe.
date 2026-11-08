import tkinter as tk
import keyboard
import mouse
import webbrowser
import time

# URL focada em desenhos da Bíblia em português
LINK_YOUTUBE = "https://youtube.com"

def fechar_programa():
    print("Saindo do Modo Bebê com segurança...")
    # Desativa todos os bloqueios antes de fechar
    keyboard.unhook_all()
    mouse.unhook_all()
    raiz.destroy()

def bloquear_tudo(evento=None):
    # Ignora absolutamente qualquer comando do teclado que não seja o de saída
    return False

def bloquear_clique(evento=None):
    # Ignora qualquer clique do mouse fora da área do vídeo ou no sistema
    return False

# 1. Configurando a janela do Python como uma cortina de proteção total
raiz = tk.Tk()
raiz.title("Modo Bebê")

# Força a tela a ficar preta e ocupar 100% do monitor (cobrindo o botão da Microsoft)
raiz.configure(bg='black')
raiz.attributes("-fullscreen", True)
raiz.attributes("-topmost", True) # Garante que nada fica na frente dessa tela

# 2. Ativando o bloqueio pesado de Hardware (Teclado e Mouse)
# Trava o teclado inteiro (Windows, Alt+Tab, Ctrl+Alt+Del visuais, etc)
keyboard.hook(bloquear_tudo, suppress=True)

# Trava o mouse para não interagir com o Windows ou barras de tarefas
mouse.hook(bloquear_clique)

# 3. Configura a única saída possível: a tecla ESC
keyboard.add_hotkey('esc', fechar_programa)

# 4. Abre o YouTube automaticamente por cima de tudo
# Aguarda 1 segundo para garantir que a proteção de tela está ativa primeiro
raiz.after(1000, lambda: webbrowser.open(LINK_YOUTUBE))

# Mantém a cortina de proteção rodando em loop
raiz.mainloop()
