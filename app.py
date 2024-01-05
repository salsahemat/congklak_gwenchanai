import tkinter as tk
from congklakGame import CongklakGUI


def main():
  # Membuat instance Tkinter untuk aplikasi GUI
    root = tk.Tk()

    # Membuat objek CongklakGUI yang akan menangani antarmuka pengguna
    app = CongklakGUI(root)

    # Memulai loop utama Tkinter untuk menampilkan GUI dan menunggu interaksi pengguna
    root.mainloop()
    
if __name__ == "_main_":
    main()