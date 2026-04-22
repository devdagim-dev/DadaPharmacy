from kivy.app import App
from kivy.uix.label import Label
import threading
from flask import Flask
import sqlite3

# --- 1. የ Flask ክፍል ---
flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return "Dada Pharmacy Server is Running!"

def run_flask():
    # ለአንድሮይድ 127.0.0.1 መጠቀም ግዴታ ነው
    flask_app.run(host='127.0.0.1', port=5000)

# --- 2. የ Kivy ክፍል (ለአንድሮይድ አፑ) ---
class PharmacyApp(App):
    def build(self):
        # Flaskን በጀርባ (Background thread) ያስጀምረዋል
        threading.Thread(target=run_flask, daemon=True).start()
        
        # አፑ ሲከፈት የሚታይ ጽሁፍ
        return Label(text="Dada Pharmacy App\n\nServer is starting...")

if __name__ == '__main__':
    PharmacyApp().run()
