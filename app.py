#!/usr/bin/python3
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
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
