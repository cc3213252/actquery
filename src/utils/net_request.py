__author__ = 'yudan.chen'

import requests
import json


def fetch(uri, data=None, method="GET"):
    headers = {'Content-Type': 'application/json',}
    host = 'https://openapi.billbear.cn'
  #  host = 'http://127.0.0.1:7693'

    url = '{}{}'.format(host, uri)
    if method.upper() == 'GET':
        url += '?' + '&'.join(['{}={}'.format(k, v, k, v) for k, v in data.items()])
    return requests.request(method.upper(), url,  headers=headers, data=json.dumps(data))