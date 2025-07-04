import tkinter as tk
from Nasa_img import *

root = tk.Tk()
root.title("NASA Image Explorer")
root.geometry("400x400")

#APOD
tk.Label(root, text="Astronomy Picture of the Day").pack()
tk.Button(root, text="Fetch APOD", command=fetch_apod).pack()

#separator
tk.Label(root, text="").pack()

#Mars Rover
tk.Label(root, text="Mars Rover Photos").pack()
tk.Label(root, text="Sol (Martian day):").pack()
sol_entry = tk.Entry(root)
sol_entry.pack()

camera_list = ["FHAZ", "RHAZ", "NAVCAM", "MAST", "CHEMCAM", "MAHLI", "MARDI"]
tk.Label(root, text="Camera:").pack()
camera_var = tk.StringVar()
camera_var.set(camera_list[0])  # default selection
camera_menu = tk.OptionMenu(root, camera_var, *camera_list)
camera_menu.pack()

tk.Label(root, text="Page Number:").pack()
page_entry = tk.Entry(root)
page_entry.pack()

tk.Button(root, text="Fetch Mars Image", command=lambda: fetch_mars_images(sol_entry, camera_var, page_entry)).pack()

root.mainloop()