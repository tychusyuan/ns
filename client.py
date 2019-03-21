#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests,json

if __name__ == "__main__":
    data={
        "":"",
        "":""
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url='url', headers=headers, data=json.dumps(data))