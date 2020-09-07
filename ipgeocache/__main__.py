import os
import sys

from . import get as get_ip_info


def main():
    assert (
        "IPINFO_TOKEN" in os.environ
    ), "Couldn't find the IPINFO_TOKEN environment variable!"
    if len(sys.argv) <= 1:
        print(
            "Must provide IP address to geolocate as the first argument!",
            file=sys.stderr,
        )
        sys.exit(1)
    for k, v in get_ip_info(sys.argv[1]).items():
        print(f"{k}={v}")


if __name__ == "__main__":
    main()
