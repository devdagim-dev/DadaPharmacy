from kivy.app import App
from kivy.uix.label import Label
import threading
from flask import Flask

# Flask ክፍል
flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return "Dada Pharmacy Server is Running!"

def run_flask():
    # host='0.0.0.0' ማድረጉ ከአንድሮይድ ጋር ይበልጥ ይስማማል
    flask_app.run(host='0.0.0.0', port=5000)

# Kivy ክፍል
class PharmacyApp(App):
    def build(self):
        # daemon=True ሰርቨሩ ከአፑ ጋር አብሮ እንዲዘጋ ያደርጋል
        threading.Thread(target=run_flask, daemon=True).start()
        return Label(text="Dada Pharmacy App\nServer is running on port 5000")

if __name__ == '__main__':
    PharmacyApp().run()
