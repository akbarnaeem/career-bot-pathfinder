
import sqlite3
import os

def create_db():
    if not os.path.exists("career_data.db"):
        conn = sqlite3.connect("career_data.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS careers (
            domain TEXT, role TEXT, avg_salary INTEGER, demand TEXT
        )''')
        cursor.executemany("INSERT INTO careers VALUES (?, ?, ?, ?)", [
            ("Data Science", "Data Analyst", 600000, "High"),
            ("Data Science", "ML Engineer", 900000, "High"),
            ("Psychology", "Counselor", 500000, "Moderate"),
            ("Design", "UX Designer", 700000, "Growing"),
            ("Design", "Graphic Designer", 450000, "Stable"),
        ])
        conn.commit()
        conn.close()

create_db()

def get_career_suggestions(domains):
    conn = sqlite3.connect("career_data.db")
    cursor = conn.cursor()
    results = []
    for domain in domains:
        cursor.execute("SELECT role, avg_salary, demand FROM careers WHERE domain=?", (domain,))
        rows = cursor.fetchall()
        for row in rows:
            results.append({
                "domain": domain,
                "role": row[0],
                "avg_salary": row[1],
                "demand": row[2]
            })
    conn.close()
    return results
