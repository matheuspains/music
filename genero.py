import tkinter as tk
from tkinter import messagebox
import random

class GeradorGeneroAleatorio:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Gênero Musical Aleatório")

        # Lista de gêneros musicais
        self.generos = [
            "Pop", "Rock", "Hip Hop", "R&B", "Eletrônica",
            "Country", "Jazz", "Blues", "Clássica",
            "Reggae", "Metal", "Folk", "Indie", "Gospel", "Punk"
        ]

        # Rótulo para exibir o gênero escolhido
        self.rotulo_genero = tk.Label(root, text="Gênero Musical:")
        self.rotulo_genero.pack(pady=10)

        # Botão para gerar um novo gênero
        self.botao_gerar = tk.Button(root, text="Gerar Gênero", command=self.gerar_genero)
        self.botao_gerar.pack(pady=10)

    def gerar_genero(self):
        # Escolhe um gênero aleatório da lista
        genero_aleatorio = random.choice(self.generos)

        # Exibe o gênero escolhido em um rótulo
        self.rotulo_genero["text"] = f"Gênero Musical: {genero_aleatorio}"

        # Mostra uma caixa de diálogo com o gênero escolhido
        messagebox.showinfo("Gênero Musical Aleatório", f"Seu gênero musical aleatório é: {genero_aleatorio}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeradorGeneroAleatorio(root)
    root.mainloop()
