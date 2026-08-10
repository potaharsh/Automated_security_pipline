import os
import sqlite3
from fastapi import FastAPI, Query

app = FastAPI(title="DevSecOps Vulnerable Demo App")

# Secret loaded from environment variable, not hardcoded
AWS_DEMO_SECRET = os.getenv("AWS_DEMO_SECRET", "default_safe_value")

@app.get("/")
def home():
    return {"status": "running", "service": "user-service"}

@app.get("/search")
def search_user(username: str = Query(...)):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Parameterized query — prevents SQL injection
    query = "SELECT * FROM users WHERE username = ?"

    try:
        cursor.execute(query, (username,))
        return {"users": cursor.fetchall()}
    finally:
        conn.close()
