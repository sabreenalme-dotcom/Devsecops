from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

SECRET_KEY = "hardcoded-secret-key-abc123"
DB_PASSWORD = "admin123"
API_KEY = "sk-prod-9f8e7d6c5b4a3210feedbeef"



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
    <h2>Login</h2>
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
    query = (
        "SELECT * FROM users WHERE username = '"
        + username
        + "' AND password = '"
        + password
        + "'"
    )
    cursor = conn.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        return f"""
        <h3 style='color:green'>✓ Login successful! Welcome, {username}</h3>
        <hr>
        <b>SQL Query executed:</b>
        <pre style='background:#ffecec;padding:10px'>{query}</pre>
        <p style='color:red'><b>VULNERABILITY:</b> The query was built using string concatenation.<br>
        An attacker bypassed authentication using SQL Injection.</p>
        """
    return f"""
        <h3 style='color:red'>✗ Invalid credentials.</h3>
        <hr>
        <b>SQL Query executed:</b>
        <pre style='background:#f0f0f0;padding:10px'>{query}</pre>
        """

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
