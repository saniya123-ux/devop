from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        db = mysql.connector.connect(
            host="db",
            user="appuser",
            password=os.environ["DB_PASSWORD"],
            database="mydatabase"
        )
        cursor = db.cursor()
        cursor.execute("SELECT 'Connected to MySQL successfully!'")
        result = cursor.fetchone()[0]
        cursor.close()
        db.close()
        return f"""
        <html>
        <body style="font-family:Arial;text-align:center;margin-top:100px">
            <h1>Docker Multi-Container Application</h1>
            <h2>Flask Web Server Running</h2>
            <p style="color:green">{result}</p>
        </body>
        </html>
        """
    except mysql.connector.Error as e:
        return f"Database connection failed: {e}", 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

