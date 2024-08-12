import os
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visor de Imágenes")
        self.root.geometry("800x600")

        self.label = Label(root)
        self.label.pack()

        self.prev_button = Button(root, text="Anterior", command=self.show_prev_image)
        self.prev_button.pack(side="left", padx=10)

        self.next_button = Button(root, text="Siguiente", command=self.show_next_image)
        self.next_button.pack(side="right", padx=10)

        self.image_list = []
        self.current_image = 0

        self.load_images()

        if self.image_list:
            self.show_image(0)
        else:
            self.label.config(text="No se encontraron imágenes en la carpeta.")

    def load_images(self):
        folder_selected = filedialog.askdirectory()
        for file in os.listdir(folder_selected):
            if file.endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
                self.image_list.append(os.path.join(folder_selected, file))

    def show_image(self, index):
        image_path = self.image_list[index]
        image = Image.open(image_path)
        image = image.resize((800, 600), Image.ANTIALIAS)
        image_tk = ImageTk.PhotoImage(image)

        self.label.config(image=image_tk)
        self.label.image = image_tk

    def show_prev_image(self):
        if self.image_list:
            self.current_image = (self.current_image - 1) % len(self.image_list)
            self.show_image(self.current_image)

    def show_next_image(self):
        if self.image_list:
            self.current_image = (self.current_image + 1) % len(self.image_list)
            self.show_image(self.current_image)

if __name__ == "__main__":
    root = Tk()
    app = ImageViewer(root)
    root.mainloop()
