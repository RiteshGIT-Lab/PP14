import configparser
import json
import sqlite3
from flask import Flask, jsonify

CONFIG_FILE = 'config.ini'
DB_FILE = 'config.db'

def read_config(file_path):
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        data = {}
        for section in config.sections():
            data[section] = dict(config.items(section))
        return data
    except Exception as e:
        print(f"Error reading config file: {e}")
        return None

def save_to_db(data, db_file):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS config_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT
            )
        ''')
        cursor.execute('DELETE FROM config_data')  # Clear previous data
        cursor.execute('INSERT INTO config_data (data) VALUES (?)', (json.dumps(data),))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error saving to database: {e}")

def fetch_from_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute('SELECT data FROM config_data ORDER BY id DESC LIMIT 1')
        row = cursor.fetchone()
        conn.close()
        if row:
            return json.loads(row[0])
        return {}
    except Exception as e:
        print(f"Error fetching from database: {e}")
        return {}

app = Flask(__name__)

@app.route('/config', methods=['GET'])
def get_config():
    data = fetch_from_db(DB_FILE)
    return jsonify(data)

if __name__ == "__main__":
    config_data = read_config(CONFIG_FILE)
    if config_data:
        print("Configuration File Parser Results:")
        for section, values in config_data.items():
            print(f"{section}:")
            for k, v in values.items():
                print(f"- {k}: {v}")
        save_to_db(config_data, DB_FILE)
    else:
        print("Failed to parse configuration file.")

    # Uncomment below to run Flask server
    # app.run(port=5000)