import tkinter as tk
import random
import pygame
from PIL.ImageTk import PhotoImage

def generate_key():
    # Retrieve the value entered in the text input field
    first_part = text_field.get()

    # Generate the key according to the rules specified in the variant
    block1 = first_part[4:7]
    block2 = first_part[1:3]
    block3 = str(int(block1) + int(block2))
    key = block1 + block2 + block3
    for i in range(len(key), 16):
        key += random.choice(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

    # Set the text of the label to the generated key
    key_label['text'] = key


# Create a new tkinter window
window = tk.Tk()
window.geometry("1000x700")

# addbackground image
bg = PhotoImage(file='bob.png')
label_img = tk.Label(window, image=bg)
label_img.place(x=0, y=0)


# Set the window title and background color
window.title("Key Generator")
window.configure(bg='white')

# Add a text input field to allow the user to enter the first part of the key
generate_button = tk.Button(window, text="Введите любые 8 цифр", font=("Arial Black", 15), bg='white')
generate_button.pack(pady=20)

text_field = tk.Entry(window, font=("Times New Roman", 20), bg='white')
text_field.pack(pady=70)

# Add a start button to initiate the key generation process

generate_button = tk.Button(window, text="СГЕНЕРИРОВАТЬ КЛЮЧ", font=("Times New Roman", 20), bg='light blue', command=lambda: [generate_key()])
generate_button.pack(pady=50)

# Add a label to display the generated key
key_label = tk.Label(window, text="", font=("Times New Roman", 20), bg='light blue')
key_label.pack(pady=50)

# play the music
pygame.mixer.init()
def play():
    pygame.mixer.music.load('Spongebob_Squarepants_Song.mp3')
    pygame.mixer.music.play(loops=999)

title = tk.Label(window, text='Music', bd=9, font=('times new roman', 30), bg='orange', fg='orange')
play()

window.mainloop()
