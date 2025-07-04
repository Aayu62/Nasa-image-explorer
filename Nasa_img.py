import tkinter as tk
from tkinter import messagebox

def fetch_apod():
    import requests
    import webbrowser
    
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key" : "DEMO_KEY"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        title = data.get("title" , "No Title")
        date = data.get("date" , "No Date")
        explanation = data.get("explanation", "No Explanation")
        img_url = data.get("url", "")

        #display in popup
        info = f"Title: {title}\nDate: {date}\n\n{explanation}"
        tk.messagebox.showinfo("APOD Info", info)

        #open image
        if img_url:
            webbrowser.open(img_url)
        
    else:
        tk.messagebox.showerror("Error", "Failed to fetch APOD")

def fetch_mars_images(sol_entry, camera_entry, page_entry):
    import requests
    import webbrowser

    # Get user input from entry boxes
    sol = sol_entry.get()
    camera = camera_entry.get()
    page = page_entry.get()

    # Validate inputs
    if not sol.isdigit() or not page.isdigit():
        messagebox.showerror("Invalid Input", "Sol and Page must be numbers.")
        return

    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    params = {
        "sol": int(sol),
        "camera": camera,
        "page": int(page),
        "api_key": "DEMO_KEY"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        photos = data.get("photos", [])
        if not photos:
            messagebox.showinfo("No Images", "No photos found for the given inputs.")
            return

        # Open the first 5 photos
        for i, photo in enumerate(photos[:5]):
            img_url = photo["img_src"]
            webbrowser.open(img_url)

        messagebox.showinfo("Success", f"Opened {min(5, len(photos))} image(s) in your browser.")
    else:
        messagebox.showerror("Error", f"Failed to fetch Mars photos.\nStatus Code: {response.status_code}")
