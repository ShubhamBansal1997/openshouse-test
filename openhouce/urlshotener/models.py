from django.db import models

from openhouce.base.models import TimeStampedUUIDModel


class ShortURL(TimeStampedUUIDModel):
    """
    url - url to be shorten
    shorten_url_code - shortend url code
    """
    url = models.TextField(null=False, blank=False)
    shorten_url_code = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = 'ShortURL'
        verbose_name_plural = 'ShortURLs'
        ordering = ['-created_at']
