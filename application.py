import logging
import logging.config

from configs.configsettings import logconfig
from utils.filehelpers import filehelper
from services.process_rank import process_rank
import datetime
import json
import time
import orjson
import rapidjson
# from utils.objecthelpers import  helper

def mappingdata(obj: object):
    print(obj.__dict__.keys())

def benchmark(name, dumps):
    start = time.time()
    for i in range(1000000):
        dumps(m)
    print(name, time.time() - start)

def main():
    ## khởi tạo logging
    logging_config = filehelper.readyalmfile(logconfig.logconfigfile)
    logging.config.dictConfig(logging_config)
    ## end khởi tạo logging
    print("{} start".format(datetime.datetime.now()))
    _process_rank = process_rank()
    _process_rank.qlt_xhdn()

    print("{} done!".format(datetime.datetime.now()))
    print("Done !")

if __name__ == '__main__':
    # some JSON:
    x = '{ "name":"John", "age":30, "city":"New York"}'

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(y["age"])

    # a Python object (dict):
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    # convert into JSON:
    y = json.dumps(x)

    # the result is a JSON string:
    print(y)

    m = {
        "timestamp": 1556283673.1523004,
        "task_uuid": "0ed1a1c3-050c-4fb9-9426-a7e72d0acfc7",
        "task_level": [1, 2, 1],
        "action_status": "started",
        "action_type": "main",
        "key": "value",
        "another_key": 123,
        "and_another": ["a", "b"],
    }

    benchmark("Python", json.dumps)
    # orjson only outputs bytes, but often we need unicode:
    benchmark("orjson", lambda s: str(orjson.dumps(s), "utf-8"))
    benchmark("rapidjson", rapidjson.dumps)
    #main()
#
# from datetime import datetime
#
# datetime.today().strftime('%Y-%m-%d')
# Additionally, for anyone also looking for a zero-padded Hour, Minute, and Second at the end: (Comment by Gabriel Staples)
#
# datetime.today().strftime('%Y-%m-%d-%H:%M:%S')