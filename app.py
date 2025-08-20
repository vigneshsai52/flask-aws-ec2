from flask import Flask, render_template_string, request, redirect, url_for
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Simple in-memory users database
users = {}

# Home route
@app.route("/")
def home():
    return "🚀 Secure Flask App Running on AWS EC2!"

# Signup route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = bcrypt.generate_password_hash(request.form["password"]).decode("utf-8")
        users[username] = password
        return redirect(url_for("login"))
    return render_template_string("""
        <h2>Signup</h2>
        <form method="POST">
            Username: <input name="username"><br>
            Password: <input type="password" name="password"><br>
            <button type="submit">Signup</button>
        </form>
    """)

# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and bcrypt.check_password_hash(users[username], password):
            return f"<h2>Welcome, {username} ✅</h2>"
        else:
            return "❌ Invalid username or password"
    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            Username: <input name="username"><br>
            Password: <input type="password" name="password"><br>
            <button type="submit">Login</button>
        </form>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
