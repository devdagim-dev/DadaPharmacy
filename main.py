from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# ዳታቤዝ ዝግጅት
def init_db():
    conn = sqlite3.connect('pharmacy.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS medicines 
                 (id INTEGER PRIMARY KEY, name TEXT, price REAL, stock INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS sales 
                 (id INTEGER PRIMARY KEY, med_id INTEGER, quantity INTEGER, total REAL, date TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inventory')
def inventory():
    conn = sqlite3.connect('pharmacy.db')
    c = conn.cursor()
    c.execute("SELECT * FROM medicines")
    meds = c.fetchall()
    conn.close()
    return render_template('inventory.html', meds=meds)

@app.route('/add_med', methods=['POST'])
def add_med():
    name = request.form['name']
    price = request.form['price']
    stock = request.form['stock']
    conn = sqlite3.connect('pharmacy.db')
    c = conn.cursor()
    c.execute("INSERT INTO medicines (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
    conn.commit()
    conn.close()
    return redirect(url_for('inventory'))

@app.route('/sell', methods=['GET', 'POST'])
def sell():
    conn = sqlite3.connect('pharmacy.db')
    c = conn.cursor()
    if request.method == 'POST':
        med_id = request.form['med_id']
        qty = int(request.form['quantity'])
        c.execute("SELECT price, stock FROM medicines WHERE id=?", (med_id,))
        res = c.fetchone()
        if res and res[1] >= qty:
            total = res[0] * qty
            c.execute("UPDATE medicines SET stock = stock - ? WHERE id=?", (qty, med_id))
            c.execute("INSERT INTO sales (med_id, quantity, total, date) VALUES (?, ?, ?, ?)",
                      (med_id, qty, total, datetime.now().strftime("%Y-%m-%d")))
            conn.commit()
    c.execute("SELECT * FROM medicines")
    meds = c.fetchall()
    conn.close()
    return render_template('sell.html', meds=meds)

@app.route('/report')
def report():
    conn = sqlite3.connect('pharmacy.db')
    c = conn.cursor()
    c.execute("SELECT SUM(total) FROM sales")
    total_sales = c.fetchone()[0] or 0
    c.execute("SELECT strftime('%m', date), SUM(total) FROM sales GROUP BY strftime('%m', date)")
    monthly = c.fetchall()
    conn.close()
    return render_template('report.html', total=total_sales, monthly=monthly)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
