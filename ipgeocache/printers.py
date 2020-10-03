import json


def default_printer(data):
    for k, v in data.items():
        print(f"{k}={v}")


def json_printer(data):
    print(json.dumps(data, indent=4, sort_keys=True))
