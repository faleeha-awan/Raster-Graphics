import tkinter as tk
from tkinter import colorchooser

class PixelArtApp:
    def __init__(self, root, pixel_size=20, grid_width=20, grid_height=20):
        self.root = root
        self.pixel_size = pixel_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.current_color = 'black'
        
        self.canvas = tk.Canvas(root, width=self.grid_width * self.pixel_size,
                                height=self.grid_height * self.pixel_size)
        self.canvas.pack()
        
        self.canvas.bind('<Button-1>', self.paint_pixel)
        self.create_color_palette()
        
        self.draw_grid()
        
    def draw_grid(self):
        for i in range(0, self.grid_width * self.pixel_size, self.pixel_size):
            for j in range(0, self.grid_height * self.pixel_size, self.pixel_size):
                self.canvas.create_rectangle(i, j, i + self.pixel_size, j + self.pixel_size, outline='gray')

    def create_color_palette(self):
        colors = ['red', 'green', 'blue', 'yellow', 'black', 'white']
        for color in colors:
            button = tk.Button(self.root, bg=color, width=2, command=lambda col=color: self.select_color(col))
            button.pack(side='left')
        
        # Button to choose custom color
        custom_color_button = tk.Button(self.root, text='Choose Color', command=self.choose_custom_color)
        custom_color_button.pack(side='left')

    def select_color(self, color):
        self.current_color = color
    
    def choose_custom_color(self):
        color_code = colorchooser.askcolor(title="Choose color")[1]
        if color_code:
            self.current_color = color_code
    
    def paint_pixel(self, event):
        x = (event.x // self.pixel_size) * self.pixel_size
        y = (event.y // self.pixel_size) * self.pixel_size
        self.canvas.create_rectangle(x, y, x + self.pixel_size, y + self.pixel_size, fill=self.current_color, outline='gray')

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Pixel Art')
    app = PixelArtApp(root)
    root.mainloop()
