from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/api/utc_time', methods=['GET'])
def get_utc_time():
    utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    return {"time": utc_time}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
