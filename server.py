#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

nameservice = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify(nameservice)
    else:
        service = request.get_json()
        request.
        nameservice[service["code"]] = service


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
