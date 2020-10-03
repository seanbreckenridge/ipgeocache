import click

from .printers import default_printer, json_printer
from . import get as get_ip_info


@click.command()
@click.option("--ipinfo-token",
              help="Authentication token to use ipinfo API. Consult https://ipinfo.io/signup", envvar="IPINFO_TOKEN")
@click.option("--json", is_flag=True)
@click.argument("ip")
def main(ip, ipinfo_token, json):
    """Gets geolocation for an IP

    IP is public internet protocol address to be geolocated
    """
    if ipinfo_token is None:
        click.secho("Couldn't find the IPINFO_TOKEN environment variable!\n"
                    "Set it on IPINFO_TOKEN or pass from CLI --ipinfo-token", fg="red")
        return

    printer = default_printer
    if json:
        printer = json_printer

    printer(get_ip_info(ip))


if __name__ == "__main__":
    main()
