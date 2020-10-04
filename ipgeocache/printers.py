import json

import click

from . import Json


def default_printer(data: Json) -> None:
    for k, v in data.items():
        click.echo(f"{k}={v}")


def json_printer(data: Json) -> None:
    click.echo(json.dumps(data, indent=4, sort_keys=True))
