from rest_framework.renderers import JSONRenderer


class OpenhouceApiRenderer(JSONRenderer):
    media_type = 'application/vnd.openhouce+json'
