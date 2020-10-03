## ipgeocache

A small cache layer for IP geolocation info.

```python
import ipgeocache
ipgeocache.get("<some ip address>")
```

If that IP has been requested before, it returns the information from cache. Else, it requests out to <https://ipinfo.io>

This requires you to get an access token from [here](https://ipinfo.io/signup), can do 50,000 lookups per month as long as you're using it for non-commercial projects.

After setting the `IPINFO_TOKEN` environment variable:

```python
>>> import ipgeocache, logzero
>>> ipgeocache.get("8.8.8.8", logger=logzero.logger)["hostname"]
[D 200906 17:56:31 __init__:62] Cache Miss: 8.8.8.8, requesting and writing to /home/sean/.local/share/ipgeocache/8.8.8.8
'dns.google'

>>> ipgeocache.get("8.8.8.8", logger=logzero.logger)["hostname"]
[D 200906 17:56:35 __init__:58] Cache Hit: 8.8.8.8, reading /home/sean/.local/share/ipgeocache/8.8.8.8
'dns.google'

>>> ipgeocache.get("8.8.8.8")
{'ip': '8.8.8.8',
 'hostname': 'dns.google',
 'city': 'Mountain View',
 'region': 'California',
 'country': 'US',
 'loc': '37.4056,-122.0775',
 'org': 'AS15169 Google LLC',
 'postal': '94043',
 'timezone': 'America/Los_Angeles'}
```

Purpose is to just be a thin wrapper that caches this info, so I don't have to think about it for my [random projects](https://github.com/seanbreckenridge/HPI#readme).

The full function signature is:

```python
ipgeocache.get(ip_address: str,
              token: Optional[str] = None,
              cache_dir: Optional[str] = None,
              logger: Optional[logging.Logger] = None) -> Dict[str, Any]

    """
    Get geolocation info for an IP address

    optional parameters:
    token: ipinfo token to use, if IPINFO_TOKEN not set as an environment variable
    cache_dir: directory to use for cache, overrides default (XDG_DATA_DIR/ipgeocache) if given
    logger: a logger to send cache hit/miss info out on
    """
```

Also installs a basic `ipgeocache` script, which you can pass an IP address to:

```
$ ipgeocache --help
Usage: ipgeocache [OPTIONS] IP

  Gets geolocation information for an IP address

  For example: 'ipgeocache 192.30.255.112'

Options:
  --ipinfo-token TEXT  Authentication token to use ipinfo API.
                       Consult https://ipinfo.io/signup

  --json               Print geolocation info as JSON
  --help               Show this message and exit.
```

```
$ ipgeocache --json 8.8.8.8
{
    "city": "Mountain View",
    "country": "US",
    "hostname": "dns.google",
    "ip": "8.8.8.8",
    "loc": "37.4056,-122.0775",
    "org": "AS15169 Google LLC",
    "postal": "94043",
    "region": "California",
    "timezone": "America/Los_Angeles"
}
```

Also accessible like `python -m ipgeocache`

### Installation

Requires `python3.6+`

To install with pip, run:

    pip install git+https://github.com/seanbreckenridge/ipgeocache

