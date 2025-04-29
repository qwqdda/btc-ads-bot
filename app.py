
from flask import Flask
import subprocess
import threading

app = Flask(__name__)

def run_bot():
    subprocess.call(["python", "main.py"])

@app.route('/')
def index():
    return "Bot is running."

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=8080)
