import pymysql
import config

conn = pymysql.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    db=config.DB_NAME,
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)
cur = conn.cursor()

try:
    cur.execute("DELETE FROM memo WHERE id = (%s)", (1))
    conn.commit()
except Exception as e:
    conn.rollback()
    print("오류 발생: ", e)
finally:
    conn.close()
