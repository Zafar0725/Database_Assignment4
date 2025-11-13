import time
import mysql.connector as mysql

DB = dict(host="127.0.0.1", port=3307, user="appuser", password="apppass", database="appdb")

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
    cur.execute("INSERT INTO subscribers (email, name) VALUES (%s, %s)", ("user1@mail.com", "User One"))
    db.commit()

    # READ
    cur.execute("SELECT id, name FROM subscribers WHERE email=%s", ("user1@mail.com",))
    row = cur.fetchone()
    assert row is not None
    sub_id = row[0]

    # UPDATE
    cur.execute("UPDATE subscribers SET name=%s WHERE id=%s", ("User One Updated", sub_id))
    db.commit()
    cur.execute("SELECT name FROM subscribers WHERE id=%s", (sub_id,))
    assert cur.fetchone()[0] == "User One Updated"

    # DELETE
    cur.execute("DELETE FROM subscribers WHERE id=%s", (sub_id,))
    db.commit()
    cur.execute("SELECT id FROM subscribers WHERE id=%s", (sub_id,))
    assert cur.fetchone() is None

    cur.close()
    db.close()
