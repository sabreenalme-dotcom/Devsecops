from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)


SECRET_KEY = os.environ.get("SECRET_KEY")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
API_KEY = os.environ.get("API_KEY")

def get_db():
    conn = sqlite3.connect("users.db")
    return conn

def init_db():
    conn = get_db()
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
    )
    conn.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'password123')")
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return """
    <h2>Login (Secured)</h2>
    <form method='POST' action='/login'>
        <input name='username' placeholder='Username'><br><br>
        <input name='password' type='password' placeholder='Password'><br><br>
        <button type='submit'>Login</button>
    </form>
    """

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

  
    conn = get_db()
    cursor = conn.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password),
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        return f"<h3>Welcome, {username}! Login successful.</h3>"
    return "<h3>Invalid credentials. Try again.</h3>"

if __name__ == "__main__":
    init_db()
    app.run(debug=False)
