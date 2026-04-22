from kivy.app import App
from kivy.uix.label import Label
import threading
from flask import Flask

# --- Flask ክፍል ---
flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return "Dada Pharmacy Server is Running!"

def run_flask():
    flask_app.run(host='127.0.0.1', port=5000)

# --- Kivy ክፍል ---
class PharmacyApp(App):
    def build(self):
        threading.Thread(target=run_flask, daemon=True).start()
        return Label(text="Dada Pharmacy App\nServer started on localhost:5000")

if __name__ == '__main__':
    PharmacyApp().run()
