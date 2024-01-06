import tkinter as tk
from PIL import Image, ImageTk
from congklakGame import CongklakGUI


def main():
  # Membuat instance Tkinter untuk aplikasi GUI
    root = tk.Tk()
    WIDTH, HEIGHT = 960, 562
    root.geometry('{}x{}'.format(WIDTH, HEIGHT))

    # Inisialisasi background gambar dengan PIL
    image = Image.open('asset/tempat2.png')
    image = image.resize((960, 560), Image.ANTIALIAS)
    background_image = ImageTk.PhotoImage(image)
    # background_image = tk.PhotoImage(file='asset/tempat1.png')
    # Membuat Label yang menampilkan gambar papan congklak (background)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Membuat objek CongklakGUI yang akan menangani antarmuka pengguna
    app = CongklakGUI(root)

    # Memulai loop utama Tkinter untuk menampilkan GUI dan menunggu interaksi pengguna
    root.mainloop()
    
if __name__ == "__main__":
    main()