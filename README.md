# NASA Image Explorer

---

## ✅ How to Run This Project on Your PC

1. **Install Python**
   - Make sure Python (version 3.x) is installed on your system.
   - Download from: https://www.python.org/downloads/

2. **Install Required Modules**
   - Open your terminal or command prompt and run:
     ```bash
     pip install requests
     ```

3. **Download the Project Files**
   - Make sure you have both of these files in the same folder:
     - `nasa_gui.py`
     - `Nasa_img.py`

4. **Run the App**
   - Open a terminal in the folder where the files are located.
   - Run the following command:
     ```bash
     python nasa_gui.py
     ```

---

## 🔍 What is an API?

An **API (Application Programming Interface)** allows one program to talk to another.  
It acts like a connector between the code and an external service.

In this project:
- We use NASA's public API.
- Python code sends a **request** to NASA's server using a web URL.
- That server **responds** with data in a format called **JSON** (which looks like a Python dictionary).
- Our code then uses that data to show useful things like:
  - A photo from a Mars rover
  - The Astronomy Picture of the Day

We don’t need to know how NASA stores its data. The API gives you only the data you ask for, based on the inputs you send.

---

## 🚀 Project Explanation

This project is a basic interface to fetch and display space-related content from **NASA’s public APIs**.

### 🔹 1. `fetch_apod()` – Astronomy Picture of the Day

- **API URL used:** `https://api.nasa.gov/planetary/apod`
- **Parameters sent:**
  - `api_key` – A required access key; we use `"DEMO_KEY"` which is free for public use.
- **What it does:**
  - Sends a GET request to the APOD API.
  - If the response is successful (`status_code == 200`), it extracts:
    - `title`: Name of the image
    - `date`: Date it was posted
    - `explanation`: A short paragraph describing the image
    - `url`: The link to the image
  - It displays the title, date, and explanation in a popup window.
  - Then it opens the image in your web browser.

---

### 🔹 2. `fetch_mars_images(sol_entry, camera_entry, page_entry)` – Mars Rover Images

- **API URL used:** `https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos`
- **Parameters sent:**
  - `sol` – The Martian day (as an integer)
  - `camera` – The rover camera to use (e.g., FHAZ, RHAZ, NAVCAM)
  - `page` – The page number of results
  - `api_key` – Access key (again using `"DEMO_KEY"`)

- **What it does:**
  - Takes user input: sol, camera, and page.
  - Sends a GET request with these inputs to NASA's Mars Rover API.
  - If the response is successful and contains photos:
    - It loops through the first 5 photos (if available).
    - For each photo, it gets the image URL from `photo["img_src"]`.
    - Then opens each image in the web browser.
  - If there are no photos for the given inputs, it shows a "No Images" message.
  - If the API call fails, it shows an error with the HTTP status code.

---

## 🧠 Summary

This project shows how APIs work in real-life:
- Send requests with parameters
- Receive structured data (JSON)
- Extract the needed values
- Display that information to users

It’s a beginner-friendly project to understand how to **call APIs**, **handle responses**, and **work with live data from real sources** like NASA.
