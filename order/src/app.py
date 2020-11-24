from flask import Flask 
import os
import requests

app = Flask(__name__)
PAYMENT_SERVICE_URL=os.getenv("PAYMENT_SERVICE_URL","http://15.207.112.139:30036")
@app.route('/api/v1/alive')
def alive():
    return {"msg": "yes"},200

@app.route('/api/v1/getlogin')
def getlogin():
    r = requests.get(PAYMENT_SERVICE_URL+"/api/v1/login")
    print(r.text)
    return r.json()
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
