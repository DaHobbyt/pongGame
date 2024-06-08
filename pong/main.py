import tkinter as tk
from tkinter import messagebox
import turtle
import random
from pvp_game import PVPGame
from pvc_game import PVCGame


class PongGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Pong Game")
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Select Game Mode:")
        self.label.pack()

        self.pvp_button = tk.Button(self.frame, text="Player vs Player", command=self.start_pvp_game)
        self.pvp_button.pack()

        self.pvc_button = tk.Button(self.frame, text="Player vs Computer", command=self.start_pvc_game)
        self.pvc_button.pack()

    def start_pvp_game(self):
        self.master.withdraw()
        self.pvp_game = PVPGame()

    def start_pvc_game(self):
        self.master.withdraw()
        self.pvc_game = PVCGame()
        self.pvc_game.play()


if __name__ == "__main__":
    root = tk.Tk()
    game = PongGame(root)
    root.mainloop()