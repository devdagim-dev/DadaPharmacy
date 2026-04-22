from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import threading
from flask import Flask, render_template
import sqlite3

# --- የ Flask ክፍል ---
app = Flask(__name__)

@app.route('/')
def index():
    return "Pharmacy App is Running!" # ለጊዜው ይህን እናድርገው

def run_flask():
    app.run(host='127.0.0.1', port=5000)

# --- የ Kivy ክፍል (ለአንድሮይድ) ---
class PharmacyApp(App):
    def build(self):
        # Flaskን በጀርባ (Background) ያስጀምረዋል
        threading.Thread(target=run_flask, daemon=True).start()
        return Label(text="Dada Pharmacy App Loading...")

if __name__ == '__main__':
    PharmacyApp().run()
