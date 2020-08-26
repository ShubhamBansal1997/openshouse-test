from openhouce.urlshotener.models import ShortURL
import hashlib


def create_shortenurl(url):
    hashids = hashlib.sha512(url.encode())
    hash_hex = hashids.hexdigest()
    shorten_url_code = hash_hex[0:10]
    url = ShortURL(url=url, shorten_url_code=shorten_url_code)
    url.save()
    return url



