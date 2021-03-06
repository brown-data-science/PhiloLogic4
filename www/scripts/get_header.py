#!/usr/bin/env python3

import os
from wsgiref.handlers import CGIHandler

from philologic.runtime import WebConfig, WSGIHandler, get_tei_header


def get_header(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=UTF-8'),
               ("Access-Control-Allow-Origin", "*")]
    start_response(status, headers)
    config = WebConfig(os.path.abspath(os.path.dirname(__file__)).replace('scripts', ''))
    request = WSGIHandler(environ, config)
    header = get_tei_header(request, config)
    yield header.encode('utf8')


if __name__ == "__main__":
    CGIHandler().run(get_header)
