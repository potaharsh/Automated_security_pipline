import sqlite3
from fastapi import FastAPI, Query

app = FastAPI(title="DevSecOps Vulnerable Demo App")

# 1. HARDCODED SECRET (Vulnerability #1)
AWS_DEMO_SECRET = os.getenv("AWS_DEMO_SECRET", "default_safe_value")


@app.get("/")
def home():
    return {"status": "running", "service": "user-service"}

@app.get("/search")
def search_user(username: str = Query(...)):
    # 2. SQL INJECTION (Vulnerability #2)
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    try:
        cursor.execute(query)
        return {"users": cursor.fetchall()}
    except Exception as e:
        return {"error": str(e)}
