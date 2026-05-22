from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = "tourists.db"

# Create database table
def init_db():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tourist_id TEXT,
        latitude TEXT,
        longitude TEXT,
        emergency_type TEXT
    )
    ''')

    conn.commit()
    conn.close()

init_db()

# Home Page
@app.route('/')
def home():
    return render_template('dashboard.html')

# SOS API
@app.route('/sos', methods=['POST'])
def sos():

    data = request.get_json()

    tourist_id = data('tourist_id')
    latitude = data('latitude')
    longitude = data('longitude')
    emergency_type = data('emergency_type')

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO alerts
    (tourist_id, latitude, longitude, emergency_type)
    VALUES (?, ?, ?, ?)
    ''', (tourist_id, latitude, longitude, emergency_type))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "SOS Alert Sent Successfully"
    })

# Get All Alerts
@app.route('/alerts')
def alerts():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alerts")

    rows = cursor.fetchall()

    conn.close()

    result = []

    for row in rows:
        result.append({
            "id": row[0],
            "tourist_id": row[1],
            "latitude": row[2],
            "longitude": row[3],
            "emergency_type": row[4]
        })

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)