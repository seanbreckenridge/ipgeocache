import json

from . import Json

def default_printer(data: Json):
    for k, v in data.items():
        print(f"{k}={v}")


def json_printer(data: Json):
    print(json.dumps(data, indent=4, sort_keys=True))
