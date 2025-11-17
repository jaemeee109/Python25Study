from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pymysql

app = FastAPI()

# React에서 호출 가능하도록 Cors 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  MariaDB 연결
DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "1234"
DB_NAME = "testdb"

def get_connection():
    """MariaDB 커넥션 하나 만들어서 반환하는 함수"""
    conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,  # 결과를 dict로 받기
    )
    return conn

@app.get("/hello")
def hello():
    return {"message" :"Hello World"}

@app.get("/db-test")
def db_test():
    """
    MariaDB에 실제로 접속해서 NOW() 값을 한 번 가져와 보는 테스트용 API
    """
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT NOW() AS now_time;")
            row = cur.fetchone()  # {'now_time': datetime객체} 형태로 옴
        return {"db_time": str(row["now_time"])}
    finally:
        conn.close()