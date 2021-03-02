import re
from urllib.parse import urlparse


def is_asset_url(url: str) -> bool:
    """Returns true if provided URL looks like asset file."""

    parsed = urlparse(url)

    if re.match(r'.*\.(ico|jpe?g|png|gif|json|css|js|txt|pdf|woff2)$', parsed.path, re.IGNORECASE):
        return True

    return False


def is_bot(user_agent: str) -> bool:
    """Returns true if provided user agent is blocked."""

    if re.match(r'pingdom|bingbot', user_agent, re.IGNORECASE):
        return True

    return False
