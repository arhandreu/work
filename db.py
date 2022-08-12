import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('reviews_db.db')
    cur = base.cursor()
    if base:
        print("База данных подключена")
    base.execute("CREATE TABLE IF NOT EXISTS reviews(id TEXT PRIMARY KEY, author TEXT, date TEXT, rate TEXT, text TEXT)")
    base.execute("CREATE TABLE IF NOT EXISTS users(id TEXT PRIMARY KEY)")
    base.commit()


def sql_add_review(data: dict):
    req = cur.execute("SELECT * FROM reviews").fetchall()
    base.commit()
    test = ''
    keys = [i[0] for i in req]
    for key, value in data.items():
        if key in keys:
            return test
        else:
            cur.execute("INSERT INTO reviews VALUES (?, ?, ?, ?, ?)", (key, value['author'], value['date'], value['rate'], value['text']))
            test += f"{value['author']} {value['date']} {value['rate']} {value['text']}\n"
    base.commit()
    return test


def add_users(id: str):
    try:
        cur.execute("INSERT INTO users VALUES(?)", (id,))
        base.commit()
        return True
    except:
        return False


def del_users(id: str):
    cur.execute("DELETE FROM users where id = ?", (id,))
    base.commit()


def show_users():
    res = cur.execute("SELECT * FROM users")
    return [i[0] for i in res]
