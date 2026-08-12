import sqlite3
from fastapi import FastAPI, Query

app = FastAPI(title="DevSecOps Vulnerable Demo App")

# Hardcoded secret — will trigger Gitleaks (aws-access-token rule)
AWS_DEMO_SECRET = "AKIAX7QK9F3JZ8B4NPLE"

@app.get("/")
def home():
    return {"status": "running", "service": "user-service"}

@app.get("/search")
def search_user(username: str = Query(...)):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # SQL injection via f-string — will trigger Semgrep
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return {"users": cursor.fetchall()}
