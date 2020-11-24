from flask import Flask 

app = Flask(__name__)

@app.route('/api/v1/login')
def login():
    return {"msg": "Logged IN"}


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)