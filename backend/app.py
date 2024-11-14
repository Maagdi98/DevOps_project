from flask import Flask, jsonify
import redis
import mysql.connector
import os

app = Flask(__name__)

# Connect to Redis with error handling
try:
    redis_client = redis.StrictRedis(
        host=os.getenv('REDIS_HOST', 'cache'),
        port=int(os.getenv('REDIS_PORT', 6379)),
        decode_responses=True
    )
except redis.ConnectionError as e:
    print(f"Redis connection error: {e}")
    redis_client = None

# Connect to MySQL with error handling
try:
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'db'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
except mysql.connector.Error as err:
    print(f"MySQL connection error: {err}")
    db = None

@app.route('/')
def index():
    if redis_client:
        redis_status = "connected"
    else:
        redis_status = "not connected"
        
    db_status = "connected" if db else "not connected"

    return jsonify(
        message="Hello from the Python backend API!",
        redis_status=redis_status,
        db_status=db_status
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
