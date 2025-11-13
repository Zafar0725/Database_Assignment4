import os
import time
import mysql.connector as mysql

# Read DB settings from environment variables (CI) with local defaults
DB = dict(
    host=os.getenv("DB_HOST", "127.0.0.1"),
    port=int(os.getenv("DB_PORT", "3307")),  # 3307 locally; CI sets 3306
    user=os.getenv("DB_USER", "appuser"),
    password=os.getenv("DB_PASS", "apppass"),
    database=os.getenv("DB_NAME", "appdb"),
)


def connect_db(retries=30, delay=1):
    last = None
    for _ in range(retries):
        try:
            return mysql.connect(**DB)
        except Exception as e:
            last = e
            time.sleep(delay)
    raise last


def test_crud_cycle():
    db = connect_db()
    cur = db.cursor()

    # CREATE
    cur.execute(
        "INSERT INTO subscribers (email, name) VALUES (%s, %s)",
        ("user1@mail.com", "User One"),
    )
    db.commit()

    # READ
    cur.execute(
        "SELECT id, name FROM subscribers WHERE email=%s",
        ("user1@mail.com",),
    )
    row = cur.fetchone()
    assert row is not None
    sub_id = row[0]

    # UPDATE
    cur.execute(
        "UPDATE subscribers SET name=%s WHERE id=%s",
        ("User One Updated", sub_id),
    )
    db.commit()
    cur.execute(
        "SELECT name FROM subscribers WHERE id=%s",
        (sub_id,),
    )
    assert cur.fetchone()[0] == "User One Updated"

    # DELETE
    cur.execute("DELETE FROM subscribers WHERE id=%s", (sub_id,))
    db.commit()
    cur.execute("SELECT id FROM subscribers WHERE id=%s", (sub_id,))
    assert cur.fetchone() is None

    cur.close()
    db.close()
