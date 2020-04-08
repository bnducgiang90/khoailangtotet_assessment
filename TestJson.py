import json
import time
import orjson
import rapidjson

def benchmark(name, dumps, m1:{}):
    start = time.time()
    for i in range(1000000):
        dumps(m1)
    print(name, time.time() - start)


if __name__ == '__main__':
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

    benchmark("Python", json.dumps, m)
    # orjson only outputs bytes, but often we need unicode:
    benchmark("orjson", lambda s: str(orjson.dumps(s), "utf-8"), m)
    benchmark("rapidjson", rapidjson.dumps, m)