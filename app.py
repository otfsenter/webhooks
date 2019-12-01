#!/usr/bin/python3
from flask import Flask, request
import json
import os

app = Flask(__name__)


def git_pull():
    os.system('cd /root/html/otfsenter.github.io/; git pull')


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    git_pull()
    return "Hello World!"
    # if request.method == 'POST':
    #     data_post = str(request.json)
    #     print(data_post)
    #     return 'true'
    # else:
    #     print('nothing')
    #     return 'false'

# if __name__ == '__main__':
#     app.run()
