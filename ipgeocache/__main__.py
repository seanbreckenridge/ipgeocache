import click

from typing import Optional

from . import get as get_ip_info
from .printers import default_printer, json_printer


@click.command()
@click.option(
    "--ipinfo-token",
    help="Authentication token to use ipinfo API. Consult https://ipinfo.io/signup",
    envvar="IPINFO_TOKEN",
)
@click.option("--json", is_flag=True, help="Print geolocation info as JSON")
@click.argument("ip")
def main(ip: str, ipinfo_token: Optional[str], json: bool) -> None:
    """
    Gets geolocation information for an IP address

    For example: 'ipgeocache 192.30.255.112'
    """
    if ipinfo_token is None:
        click.secho(
            "Could not find ipinfo access token!\n"
            "Set the IPINFO_TOKEN environment variable or pass the --ipinfo-token flag",
            fg="red",
        )
        return

    printer = default_printer
    if json:
        printer = json_printer

    printer(get_ip_info(ip))


if __name__ == "__main__":
    main()
