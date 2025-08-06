import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import random
import requests
import pyttsx3

# ------------------ DATABASE FUNCTIONS ------------------ #

def connect_db():
    return sqlite3.connect("users.db")

def create_user_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def validate_login(username, password):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cur.fetchone()
    conn.close()
    return result is not None

# ------------------ TTS & DICTIONARY FUNCTIONS ------------------ #

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

word_list = ["apple", "friend", "book", "learn", "happy", "computer", "sun", "rain", "kind", "smile"]

def get_definition(word):
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        data = response.json()
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
        example = data[0]['meanings'][0]['definitions'][0].get('example', 'No example available.')
        return definition, example
    except:
        return None, None

# ------------------ BACKGROUND SETTER ------------------ #

def set_background(root, image_path):
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((1500, 800), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    background_label = tk.Label(root, image=bg_photo)
    background_label.image = bg_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

# ------------------ DICTIONARY GUI ------------------ #

def launch_dictionary(username):
    root = tk.Tk()
    root.title("Accessible Dictionary / शब्दकोश")
    root.geometry("500x420")
    root.resizable(False, False)

    set_background(root, r"C:\Users\Jyoti Shekhawat\OneDrive\Desktop\blue.webp")

    word_of_the_day = random.choice(word_list)
    definition, _ = get_definition(word_of_the_day)

    tk.Label(root, text=f"Hello {username} / नमस्ते {username}", font=("Arial", 12, "bold"), bg="#ffffff").pack(pady=5)
    tk.Label(root, text=f"🌟 Word of the Day / आज का शब्द: {word_of_the_day}", font=("Arial", 12, "bold"), fg="blue", bg="#ffffff").pack(pady=5)
    tk.Label(root, text=f"{definition}", wraplength=450, font=("Arial", 11), bg="#ffffff").pack(pady=2)

    entry = tk.Entry(root, font=("Arial", 12), width=30)
    entry.pack(pady=10)

    lbl_result = tk.Label(root, text="", wraplength=460, font=("Arial", 11), justify="left", bg="#ffffff")
    lbl_result.pack(pady=10)

    def search_word():
        word = entry.get().strip()
        if not word:
            messagebox.showwarning("Warning", "Please enter a word.\nकृपया एक शब्द दर्ज करें।")
            return
        definition, example = get_definition(word)
        if definition:
            lbl_result.config(text=f"Definition / अर्थ: {definition}\n\nExample / उदाहरण: {example}")
        else:
            lbl_result.config(text="Word not found / शब्द नहीं मिला।")

    def speak_result():
        text = lbl_result.cget("text")
        if text:
            speak(text)

    def clear_fields():
        entry.delete(0, tk.END)
        lbl_result.config(text="")

    # Buttons
    frame_buttons = tk.Frame(root, bg="#ffffff")
    frame_buttons.pack()

    tk.Button(frame_buttons, text="Search / खोजें", command=search_word, font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_buttons, text="Clear / साफ करें", command=clear_fields, font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_buttons, text="🔊 Speak / बोलें", command=speak_result, font=("Arial", 11)).pack(side=tk.LEFT, padx=5)

    root.mainloop()

# ------------------ LOGIN SYSTEM ------------------ #

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login / लॉगिन")
        self.root.geometry("320x250")
        set_background(self.root, r"C:\Users\Jyoti Shekhawat\OneDrive\Desktop\blue.webp")
        self.create_login_page()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        set_background(self.root, r"C:\Users\Jyoti Shekhawat\OneDrive\Desktop\blue.webp")

    def create_login_page(self):
        self.clear_screen()
        tk.Label(self.root, text="Login / लॉगिन", font=('Arial', 16), bg="#ffffff").pack(pady=10)

        tk.Label(self.root, text="Username (उपयोगकर्ता नाम)", bg="#ffffff").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password (पासवर्ड)", bg="#ffffff").pack()
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack()

        tk.Button(self.root, text="Login / लॉगिन करें", command=self.login_user).pack(pady=5)
        tk.Button(self.root, text="Register / रजिस्टर करें", command=self.create_register_page).pack()

    def create_register_page(self):
        self.clear_screen()
        tk.Label(self.root, text="Register / रजिस्टर", font=('Arial', 16), bg="#ffffff").pack(pady=10)

        tk.Label(self.root, text="Username (उपयोगकर्ता नाम)", bg="#ffffff").pack()
        self.new_username_entry = tk.Entry(self.root)
        self.new_username_entry.pack()

        tk.Label(self.root, text="Password (पासवर्ड)", bg="#ffffff").pack()
        self.new_password_entry = tk.Entry(self.root, show='*')
        self.new_password_entry.pack()

        tk.Button(self.root, text="Submit / सबमिट करें", command=self.register_user).pack(pady=5)
        tk.Button(self.root, text="Back / वापसी", command=self.create_login_page).pack()

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if validate_login(username, password):
            messagebox.showinfo("Success / सफल", f"Welcome {username}!\nस्वागत है {username}!")
            self.root.destroy()
            launch_dictionary(username)
        else:
            messagebox.showerror("Error / त्रुटि", "Invalid username or password!\nगलत उपयोगकर्ता नाम या पासवर्ड!")

    def register_user(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()

        if register_user(username, password):
            messagebox.showinfo("Success / सफल", "Registration successful!\nपंजीकरण सफल हुआ!")
            self.create_login_page()
        else:
            messagebox.showerror("Error / त्रुटि", "Username already exists!\nउपयोगकर्ता नाम पहले से मौजूद है!")

# ------------------ START THE APP ------------------ #

if __name__ == "__main__":
    create_user_table()
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
