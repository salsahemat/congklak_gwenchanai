import tkinter as tk
from congklakGame import Congklak, CongklakGUI

def main():
    root = tk.Tk()
    congklak_game = Congklak()
    app = CongklakGUI(root, congklak_game)
    root.mainloop()

if __name__ == "__main__":
    main()
