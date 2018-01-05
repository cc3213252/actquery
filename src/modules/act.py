__author__ = 'yudan.chen'

import json
from src.utils.net_request import fetch


def fetch_act_by_id(act_id):
    try:
        data = {
            "act_id": act_id
        }
        resp = fetch('/api/v1/act', data=data, method='GET')
        resp_obj = json.loads(resp.text)
        return resp_obj
    except:
        return {"title": '', 'mongo_id': ''}