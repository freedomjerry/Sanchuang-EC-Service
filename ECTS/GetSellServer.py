from flask import Flask, request, jsonify
from flask_cors import CORS
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
import subprocess
import threading
from connect2mysql import run_connection
from subprocess import PIPE
REQUEST_METHOD_MAP = {'GET': 'args', 'POST': 'form'}
executors = {
    'default': ThreadPoolExecutor(10)
}
app = Flask(__name__)
scheduler = BlockingScheduler(executors=executors)
CORS(app)

class GetSellThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        try:
            run_connection()
        except Exception as e:
            print(e)
            print("销售数据获取失败")
            return None
        # try:
        #     # subprocess.run(["bin/ects  -d sell1.txt pred.txt"])
        # except Exception as e:
        #     print(e)
        #     return None


@app.route('/ECTSServer', methods=['POST', 'GET'])
def ECTS_run():
    t = GetSellThread()
    t.start()
    a = "-d"
    b = "sell1.txt"
    c = "pred.txt"
    s = subprocess.run(["./bin/ects", a, b, c],stdout=PIPE)
    # print(type(s.stdout.decode("utf-8")))
    if s.stdout.decode("utf-8") == "1":
        return jsonify(code=1, message="Warning", result=[])
    else:
        return jsonify(code=0, message="Normal", result=[])

app.run(host='0.0.0.0', port=int("8000"), debug=True)