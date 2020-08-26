from django.http import HttpResponseRedirect
from django.shortcuts import render

from openhouce.urlshotener.models import ShortURL

def redirect_page(request, url_short_code, template_name='404.html'):
    ctx = {}
    url = None
    try:
        url_data = ShortURL.objects.get(shorten_url_code=url_short_code)
        url_data = url_data.url
    except Exception as e:
        # add logging statement later
        print("URL NOT FOUND")
    if url_data is not None:
        return HttpResponseRedirect(url_data)
    else:
        return render(request, template_name, ctx)

