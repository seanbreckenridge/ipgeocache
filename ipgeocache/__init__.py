import os
import json
import warnings
import logging

from pathlib import Path
from typing import Optional, Dict, Any
from functools import lru_cache

import requests

CACHE_DIR_NAME: str = "ipgeocache"
BASE_URL: str = "https://ipinfo.io/{}"

Json = Dict[str, Any]


@lru_cache(1)
def get_cache_dir(passed_cache: Optional[str] = None) -> Path:
    """
    Uses the cache directory given by the user, else uses the default location
    """
    if passed_cache is None:
        # use XDG dir, else ~/.local/share/
        data_dir: str = os.environ.get(
            "XDG_DATA_HOME", os.path.join(os.environ["HOME"], ".local", "share")
        )
        def_p = Path(data_dir).expanduser().absolute() / CACHE_DIR_NAME
        if not def_p.exists():
            def_p.mkdir(parents=True)
        return def_p
    else:
        user_p: Path = Path(passed_cache).expanduser().absolute()
        if not user_p.exists():
            warnings.warn(f"{user_p} cache dir doesn't exist, creating...")
            user_p.mkdir(parents=True)
        return user_p


def get_token(token: Optional[str] = None) -> str:
    """
    Get the token passed by the user, else lookup in environment
    """
    if token is not None:
        return token
    elif "IPINFO_TOKEN" in os.environ:
        return os.environ["IPINFO_TOKEN"]
    else:
        warnings.warn("No geolocation ipinfo token passed or in environment!")
        return ""


def get_from_cache_or_request(
    ip_address: str,
    ipinfo_token: str,
    cache_dir: Path,
    logger: Optional[logging.Logger],
) -> Json:
    cache_target: Path = cache_dir / ip_address.strip()
    if cache_target.exists():
        if logger is not None:
            logger.debug("Cache Hit: {}, reading {}".format(ip_address, cache_target))
        ipinfo: Json = json.loads(cache_target.read_text())
        return ipinfo
    else:
        if logger is not None:
            logger.debug(
                "Cache Miss: {}, requesting and writing to {}".format(
                    ip_address, cache_target
                )
            )
        resp = requests.get(
            BASE_URL.format(ip_address),
            headers={"Authorization": "Bearer {}".format(ipinfo_token)},
        )
        resp.raise_for_status()
        resp_json: Json = resp.json()
        with cache_target.open("w") as jf:
            json.dump(resp_json, jf)
        return resp_json


def get(
    ip_address: str,
    token: Optional[str] = None,
    cache_dir: Optional[str] = None,
    logger: Optional[logging.Logger] = None,
) -> Json:
    """
    Get geolocation info for an IP address

    optional parameters:
    token: ipinfo token to use, if IPINFO_TOKEN not set as an environment variable
    cache_dir: directory to use for cache, overrides default (XDG_DATA_DIR/ipgeocache) if given
    logger: a logger to send cache hit/miss info out on
    """
    return get_from_cache_or_request(
        ip_address, get_token(token), get_cache_dir(cache_dir), logger=logger
    )
