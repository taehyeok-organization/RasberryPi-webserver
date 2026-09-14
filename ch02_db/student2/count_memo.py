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

cur.execute("select count(*) as cnt from memo")
row = cur.fetchone()
print("메모 개수 :", row["cnt"])

conn.close()
