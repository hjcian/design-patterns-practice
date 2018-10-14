from flask import Flask, Response
from flask_restful import Resource, Api
from concurrent.futures import ThreadPoolExecutor
import time
import uuid

class DoJob(Resource):
    def __init__(self, job_executor):
        self._job_executor = job_executor

    def BGJob(self, _uuid):
        print("Task [{}] started! ".format(_uuid))
        time.sleep(3)
        print("Task [{}] is done! ".format(_uuid))

    def get(self):
        _uuid = uuid.uuid4().hex
        self._job_executor.submit(self.BGJob, _uuid)
        return Response("[{}] submit OK\n".format(_uuid), 200)

def setApiRouter(api, job_executor):
    api.add_resource(DoJob, '/do', resource_class_kwargs={"job_executor": job_executor})

def main():
    job_executor = ThreadPoolExecutor(2)
    app = Flask(__name__)
    api = Api(app)
    setApiRouter(api, job_executor)
    port = 11111
    app.run(host='0.0.0.0', port=port, threaded=True)

if __name__ == "__main__":
    main()
