from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image

new_image = None
file1_path = None
watermark_path = 'images/copyright.png'


# -------------------------------------------- Functions -------------------------------------------#
def upload_action():
    global file1_path
    file1_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Image files", "*.png")])
    if file1_path:
        change_image(file1_path)


def change_image(filepath):
    global new_image, add_watermark_btn
    new_image = PhotoImage(file=filepath)
    canvas.itemconfig(canvas_img, image=new_image)
    add_watermark_btn.grid(column=0, row=4, columnspan=2, padx=5, pady=5)


def add_watermark():
    global file1_path, watermark_path
    background = Image.open(file1_path)
    foreground = Image.open(watermark_path)
    resize_image = foreground.resize((50, 50))
    background.paste(resize_image, (0, 0), resize_image)
    final_image_path = './images/final_image.png'
    background.save(final_image_path, format='png')
    change_image(final_image_path)


def change_watermark():
    global watermark_path
    watermark_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Image files", "*.png")])


# -------------------------------------------- UI Setup --------------------------------------------#
BACKGROUND_COLOR = "#76ff33"
# Window setup
window = Tk()
# im = Image.open("hopper.ppm")
window.title('Watermark Tool')
window.config(height=800, width=800, pady=15, padx=15, bg=BACKGROUND_COLOR)

# Canvas layout
canvas = Canvas(width=400, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)
placeholder = PhotoImage(file='images/placeholder.png')
watermark_img = PhotoImage(file=watermark_path)
canvas_img = canvas.create_image(200, 200, image=placeholder)
canvas_text = canvas.create_text(200, 200, font=("Aerial", 10, "italic"))
canvas.grid(column=0, row=1, columnspan=2, padx=5, pady=5)

# Buttons
upload_btn = Button(text='upload images file', command=upload_action, highlightthickness=0)
upload_btn.grid(column=0, row=2)
watermark_preset_btn = Button(text='Change Watermark', highlightthickness=0, command=change_watermark)
watermark_preset_btn.grid(column=1, row=2)
add_watermark_btn = Button(text='Add Watermark', highlightthickness=0, command=add_watermark)

# Labels
title = Label(window, text='Watermark Tool', font=("Aerial", 15), fg='Black', bg=BACKGROUND_COLOR)
title.grid(row=0, column=0, columnspan=2)

window.mainloop()
