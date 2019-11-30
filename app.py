from flask import Flask, request

app = Flask(__name__)


@app.route('/hook', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        data_post = str(request.json)
        print(data_post)
        return 'true'
    else:
        print('nothing')
        return 'false'


if __name__ == '__main__':
    app.run()
