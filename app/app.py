
import os
import redis
from flask import Flask, jsonify

app = Flask(__name__)

# Redis connection configuration
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True,
    socket_connect_timeout=2,
    socket_timeout=2
)

@app.route("/")
def home():
    try:
        # Increment visitor count in Redis
        count = redis_client.incr("visitor_count")

        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Visitor Counter</title>
            <style>
                body {{
                    font-family: Arial;
                    text-align: center;
                    background: #f0f4f8;
                    padding-top: 100px;
                }}
                .container {{
                    background: white;
                    padding: 40px;
                    margin: auto;
                    max-width: 450px;
                    border-radius: 15px;
                    box-shadow: 0 4px 15px #ccc;
                }}
                h1 {{ color: #2563eb; }}
                .count {{
                    font-size: 55px;
                    color: #16a34a;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to Visitor Counter!</h1>
                <p>Total Website Visits</p>
                <div class="count">{count}</div>
                <p>Powered by Flask + Redis</p>
            </div>
        </body>
        </html>
        """

    except redis.RedisError:
        return "Redis database is unavailable", 503


@app.route("/health")
def health():
    try:
        redis_client.ping()
        return jsonify(status="healthy", redis="connected"), 200
    except redis.RedisError:
        return jsonify(status="unhealthy", redis="disconnected"), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
